from abc import *
from Domain.Entity.OwnedAbility import OwnedAbility
from Domain.ValueObject.RollGettableInterface import RollGettableInterface

class AbstractComparator(metaclass=ABCMeta):
    @abstractmethod
    def compare(self, dice: RollGettableInterface, ownedAbility: OwnedAbility):
        pass
