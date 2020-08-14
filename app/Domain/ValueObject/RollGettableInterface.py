from abc import *

class RollGettableInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_result(self) -> int:
        pass
