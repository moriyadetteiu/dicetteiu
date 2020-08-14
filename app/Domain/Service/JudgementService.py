from Domain.Entity.OwnedAbility import OwnedAbility
from Domain.ValueObject.RollGettableInterface import RollGettableInterface
from .Comparator.comparator_generator import generate

class JudgementService:
    def __init__(self, dice: RollGettableInterface, ownedAbility: OwnedAbility):
        self.__dice = dice
        self.__ownedAbility = ownedAbility

    def judge(self, method: str, value: int):
        comparator = generate(method)
