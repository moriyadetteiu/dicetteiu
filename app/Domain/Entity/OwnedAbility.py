from Domain.Exceptions.InvalidArgumentException import InvalidArgumentException
from Domain.ValueObject.Dice import Dice
from .Ability import Ability

class OwnedAbility:
    def __init__(self, ability: Ability, level: int):
        if level < 0 or level > 100:
            raise InvalidArgumentException('技能の熟練度は0～100にしてください')

        self.__ability = ability
        self.__level = level

    def get_ability(self) -> str:
        return self.__ability

    def get_level(self) -> int:
        return self.__level
