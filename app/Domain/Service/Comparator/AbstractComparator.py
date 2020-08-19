from abc import *
from Domain.Entity.TargetLevelGettableInterface import TargetLevelGettableInterface
from Domain.ValueObject.EffectiveValueGettableInterface import EffectiveValueGettableInterface

class AbstractComparator(metaclass=ABCMeta):
    @abstractmethod
    def compare(self, dice: EffectiveValueGettableInterface, ownedAbility: TargetLevelGettableInterface) -> bool:
        pass
