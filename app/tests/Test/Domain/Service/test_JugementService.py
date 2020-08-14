# このテストファイル内で各Comparatorのテストも行う
from unittest import TestCase
from Domain.Entity.Ability import Ability
from Domain.Entity.OwnedAbility import OwnedAbility
from Domain.Service.JudgementService import JudgementService
from Domain.Service.Comparator.AbstractComparator import AbstractComparator
from Domain.Service.Comparator.LessThanComparator import LessThanComparator
from Domain.Service.Comparator.LessEqualThanComparator import LessEqualThanComparator
from Domain.Service.Comparator.GreaterThanComparator import GreaterThanComparator
from Domain.Service.Comparator.GreaterEqualThanComparator import GreaterEqualThanComparator
from Domain.ValueObject.Dice import Dice
from .Mock.FixedDice import FixedDice

class TestJudgementService(TestCase):
    def test_greater_than(self):
        comparator = GreaterThanComparator()
        self.assert_compare_true(comparator, 10, 11)
        self.assert_compare_false(comparator, 10, 10)

    def test_greater_equal_than(self):
        comparator = GreaterEqualThanComparator()
        self.assert_compare_true(comparator, 10, 10)
        self.assert_compare_false(comparator, 10, 9)

    def test_less_than(self):
        comparator = LessThanComparator()
        self.assert_compare_true(comparator, 10, 9)
        self.assert_compare_false(comparator, 10, 10)

    def test_less_equal_than(self):
        comparator = LessEqualThanComparator()
        self.assert_compare_true(comparator, 10, 10)
        self.assert_compare_false(comparator, 10, 11)

    def assert_compare_true(self, comparator: AbstractComparator, ownedAbilityLevel: int, FixedDiceNumber: int):
        ownedAbility = self.make_owned_ability(ownedAbilityLevel)
        fixedDice = FixedDice(FixedDiceNumber)
        result = comparator.compare(fixedDice, ownedAbility)
        self.assertTrue(result)

    def assert_compare_false(self, comparator: AbstractComparator, ownedAbilityLevel: int, FixedDiceNumber: int):
        ownedAbility = self.make_owned_ability(ownedAbilityLevel)
        fixedDice = FixedDice(FixedDiceNumber)
        result = comparator.compare(fixedDice, ownedAbility)
        self.assertFalse(result)

    def make_owned_ability(self, level: int, name: str = 'test'):
        ability = Ability(name)
        return OwnedAbility(ability, level)
