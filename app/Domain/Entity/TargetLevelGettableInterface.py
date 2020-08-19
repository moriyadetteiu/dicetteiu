from abc import *

class TargetLevelGettableInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_level(self) -> int:
        pass
