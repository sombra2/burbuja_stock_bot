from src.finance.repositories.clients import YahooFinanceAPIClient


class ClientFactory:
    YAHOO_CLIENT = "yahoo"
    CLIENTS = {YAHOO_CLIENT: YahooFinanceAPIClient}

    @staticmethod
    def build(client_name: str):
        if client_name in ClientFactory.CLIENTS:
            return ClientFactory.CLIENTS[client_name]()
        else:
            raise Exception(f"Client {client_name} is not available.")
