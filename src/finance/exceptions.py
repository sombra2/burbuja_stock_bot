from src.finance.asset_type import AssetType
from src.finance.time_range import DatePeriod


class UnsupportedAssetType(Exception):
    def __init__(self, client: str, asset_type: AssetType):
        self.asset_type = asset_type
        self.client = client

    def __repr__(self):
        return f"{self.client} does not support the specified {self.asset_type} asset type."


class FinancialAPIUnavailableData(Exception):
    def __init__(self, client: str, asset_id: str, period: DatePeriod):
        self.asset_id = asset_id
        self.client = client
        self.period = period

    def __repr__(self):
        return f"{self.client} does not have data for asset_id: {self.asset_id} on period: {str(self.period)}"
