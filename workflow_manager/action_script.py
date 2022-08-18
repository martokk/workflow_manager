import traceback
from abc import abstractmethod


class ActionScript:
    @abstractmethod
    def script(self, **kwargs) -> str:
        return ""

    def run(self, **kwargs) -> str:
        try:
            return self.script(**kwargs)
        except Exception as e:
            rtn_str = f"\nERROR: Script did NOT complete successfully.\n"
            rtn_str += f"TRACEBACK: {traceback.format_exc()}\n"
            rtn_str += f"ERROR: {e}"
            return rtn_str
