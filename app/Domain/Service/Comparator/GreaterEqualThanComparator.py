from Domain.Entity.TargetLevelGettableInterface import TargetLevelGettableInterface
from Domain.ValueObject.EffectiveValueGettableInterface import EffectiveValueGettableInterface
from .AbstractComparator import AbstractComparator

class GreaterEqualThanComparator(AbstractComparator):
    def compare(self, dice: EffectiveValueGettableInterface, ownedAbility: TargetLevelGettableInterface) -> bool:
        return dice.get_result() >= ownedAbility.get_level()
