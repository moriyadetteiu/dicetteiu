from Domain.Entity.OwnedAbility import OwnedAbility
from Domain.ValueObject.RollGettableInterface import RollGettableInterface
from .AbstractComparator import AbstractComparator

class GreaterThanComparator(AbstractComparator):
    def compare(self, dice: RollGettableInterface, ownedAbility: OwnedAbility) -> bool:
        return dice.get_result() > ownedAbility.get_level()
