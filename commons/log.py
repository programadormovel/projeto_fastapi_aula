import logging


class Log:
    def __init__(self, message: str):
        self._log = logging.getLogger("uvicorn")
        self.message = message

    def info(self):
        self._log.info(self.message)

    def debug(self):
        self._log.debug(self.message)

    def error(self):
        self._log.error(self.message)

    def warning(self):
        self._log.warning(self.message)
