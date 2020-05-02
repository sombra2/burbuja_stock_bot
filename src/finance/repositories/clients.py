from abc import ABC, abstractmethod
from concurrent.futures._base import as_completed, Future
from concurrent.futures.thread import ThreadPoolExecutor
from typing import List
from datetime import datetime

import numpy
import yfinance
from pandas import DataFrame, Timestamp

from src.finance.asset import Asset, Valuation
from src.finance.asset_type import AssetType
from src.finance.exceptions import UnsupportedAssetType, FinancialAPIUnavailableData
from src.finance.time_range import DatePeriod


class AssetAPIClient(ABC):
    SUPPORTED_ASSET_TYPES = []

    def _validate_asset_type(self, asset_type: AssetType) -> None:
        if asset_type not in self.SUPPORTED_ASSET_TYPES:
            raise UnsupportedAssetType(client=self.__name__, asset_type=asset_type)

    @abstractmethod
    def fetch_asset_data(self, asset: Asset) -> Asset:
        pass


class YahooFinanceAPIClient(AssetAPIClient):
    SUPPORTED_ASSET_TYPES = [AssetType.STOCK]
    DEFAULT_CURRENCY = "USD"
    RESULT_DATE = "Date"
    RESULT_CLOSING_PRICE = "Close"
    MAX_CONCURRENCY = 4

    def fetch_asset_data(self, asset: Asset) -> Asset:
        self._validate_asset_type(asset.type)
        self.__gather_valuations(asset)
        return asset

    def __gather_valuations(self, asset: Asset) -> None:
        """Naive concurrent queue consumer"""
        cache: List[Future] = []
        with ThreadPoolExecutor(YahooFinanceAPIClient.MAX_CONCURRENCY) as thread_pool:
            while asset.are_there_valuation_requests():
                period: DatePeriod = asset.deque_requested_valuation()
                cache.append(
                    thread_pool.submit(self.__fetch_valuation, asset.id, period)
                )
        for future in as_completed(cache):
            valuation: Valuation = future.result()
            asset.update_valuation(period=valuation.period, valuation=valuation)

    def __fetch_valuation(self, asset_id: str, period: DatePeriod) -> Valuation:
        result: DataFrame = yfinance.download(
            asset_id,
            start=str(period.start_date),
            end=str(period.end_date),
            threads=True,
        )
        if len(result) == 0:
            raise FinancialAPIUnavailableData(
                client=YahooFinanceAPIClient.__name__, asset_id=asset_id, period=period
            )
        starting_price = result.at[
            min(result.index), YahooFinanceAPIClient.RESULT_CLOSING_PRICE
        ]
        ending_price = result.at[
            max(result.index), YahooFinanceAPIClient.RESULT_CLOSING_PRICE
        ]
        # TODO: The API returns 2 rows if you query just 1 day... Look for a more elegant handling of this
        if isinstance(starting_price, numpy.ndarray):
            starting_price, ending_price = starting_price[0], ending_price[0]
        return Valuation(
            period=period,
            starting_price=starting_price,
            end_price=ending_price,
            currency=YahooFinanceAPIClient.DEFAULT_CURRENCY,
        )
