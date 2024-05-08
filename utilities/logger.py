import logging
from utilities.constants import Constants


class Logger:
    def info(self, message):
        logging.info(message)

    def error(self, message):
        logging.error(message)

    def config(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(threadName)s %(asctime)s: %(message)s",
            datefmt=Constants.date_format,
        )
