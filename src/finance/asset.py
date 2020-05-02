from queue import Queue
from typing import List, Dict

from src.finance.asset_type import AssetType
from src.finance.time_range import DatePeriod


class Valuation:
    period: DatePeriod
    starting_price: float
    end_price: float
    currency: str

    def __init__(
        self, period: DatePeriod, starting_price: float, end_price: float, currency: str
    ):
        self.period = period
        self.starting_price = starting_price
        self.end_price = end_price
        self.currency = currency


# TODO: Maybe extend it instead of handling though enum AssetType (no good case for that right now)
class Asset:
    type: AssetType
    id: str
    __valuations: Dict[DatePeriod, Valuation]
    __requested_valuations: Queue

    def __init__(self, asset_id: str, asset_type: AssetType):
        self.id = asset_id
        self.type = asset_type
        self.__valuations = dict()
        self.__requested_valuations = Queue()

    def enqueue_valuation_request(self, period: DatePeriod) -> None:
        self.__requested_valuations.put(period)

    def are_there_valuation_requests(self) -> bool:
        return not self.__requested_valuations.empty()

    def deque_requested_valuation(self) -> DatePeriod:
        return self.__requested_valuations.get()

    def update_valuation(self, period: DatePeriod, valuation: Valuation) -> None:
        self.__valuations[period] = valuation

    def get_available_valuation_requests(self) -> List[DatePeriod]:
        return list(self.__valuations.keys())

    def get_valuations(self) -> Dict[DatePeriod, Valuation]:
        return self.__valuations

    def get_valuation(self, period: DatePeriod) -> Valuation:
        return self.__valuations[period]
