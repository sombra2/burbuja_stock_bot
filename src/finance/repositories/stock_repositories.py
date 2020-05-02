from typing import List, Dict

from src.finance.asset import Asset, Valuation
from src.finance.asset_type import AssetType
from src.finance.time_range import DatePeriod
from src.finance.repositories.clients import AssetAPIClient


class StocksDataRepository:

    client: AssetAPIClient

    def __init__(self, client: AssetAPIClient):
        self.client = client

    def get_stock_valuations(
        self, ticker: str, periods: List[DatePeriod]
    ) -> Dict[DatePeriod, Valuation]:
        asset = Asset(asset_id=ticker, asset_type=AssetType.STOCK)
        for period in periods:
            asset.enqueue_valuation_request(period)
        return self.client.fetch_asset_data(asset).get_valuations()
