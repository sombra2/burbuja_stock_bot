import os
import json

from src.generic_types import PythonDeserializedJSON, JSONPrimitive


class BasicConfiguration:
    """We rely on the credentials being stored in the telegram_credentials.json JSON file in the .credentials directory.
    """

    CREDENTIALS_FOLDER = ".credentials"
    TELEGRAM_CREDENTIALS_FILE = "telegram_credentials.json"
    BOT_TOKEN = "botToken"
    TELEGRAM_CHAT_ID = "telegramChatId"

    __credentials: PythonDeserializedJSON

    def __init__(self):
        self.__load_configuration()

    def __load_configuration(self):
        with open(
            os.path.join(
                BasicConfiguration.CREDENTIALS_FOLDER,
                BasicConfiguration.TELEGRAM_CREDENTIALS_FILE,
            ),
            "r",
        ) as file:
            self.credentials: PythonDeserializedJSON = json.load(file)

    def get_credential(self, credential: str) -> JSONPrimitive:
        """Throws KeyError if credential does not exist"""
        return self.__credentials[credential]
