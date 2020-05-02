import sys

from src.configuration import BasicConfiguration
from src.command_handlers import start_handler, stonk_handler
from telegram.ext import Updater
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger("main")

logger.info("Fetching credentials.")
configuration = BasicConfiguration()
updater = Updater(
    token=configuration.get_credential(BasicConfiguration.BOT_TOKEN), use_context=True
)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(stonk_handler)
updater.start_polling()
