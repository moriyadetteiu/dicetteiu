from abc import *

class EffectiveValueGettableInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_result(self) -> int:
        pass
