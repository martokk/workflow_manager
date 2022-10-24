import traceback
from abc import ABCMeta, abstractmethod

from loguru import logger


class ActionScript(metaclass=ABCMeta):
    @abstractmethod
    def script(self, **kwargs: object) -> str:
        print(f"Hello World. {kwargs=}")
        return ""

    def run(self, **kwargs: object) -> str:
        try:
            return self.script(**kwargs)
        except Exception as ex:  # pylint: disable=broad-except
            rtn_str = "\nERROR: Script did NOT complete successfully.\n"
            rtn_str += f"TRACEBACK: {traceback.format_exc()}\n"
            rtn_str += f"ERROR: {ex}"
            logger.error(rtn_str)
            return rtn_str
