# このテストファイル内で各Comparatorのテストも行う
from unittest import TestCase
from Domain.Entity.Ability import Ability
from Domain.Entity.OwnedAbility import OwnedAbility
from Domain.Service.JudgementService import JudgementService
from Domain.Service.Comparator.GreaterThanComparator import GreaterThanComparator
from Domain.ValueObject.Dice import Dice
from .Mock.FixedDice import FixedDice

class TestJudgementService(TestCase):
    def test_greater_than(self):
        comparator = GreaterThanComparator()

        ownedAbility = self.make_owned_ability(11)
        fixedDiceOfTen = FixedDice(10)
        result = comparator.compare(fixedDiceOfTen, ownedAbility)
        self.assertFalse(result)

        fixedDiceOfEleven = FixedDice(11)
        result = comparator.compare(fixedDiceOfEleven, ownedAbility)
        self.assertTrue(result)

    def make_owned_ability(self, level: int, name: str = 'test'):
        ability = Ability(name)
        return OwnedAbility(ability, level)
