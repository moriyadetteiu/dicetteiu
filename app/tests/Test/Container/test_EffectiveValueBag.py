from unittest import TestCase
from Container.EffectiveValueBag import EffectiveValueBag
from Test.Domain.Service.Mock.FixedDice import FixedDice

class TestEffectiveValueBag(TestCase):
    def test_get_result(self):
        fixedDiceValues = [1, 2, 3]

        d = FixedDice('a')

        bag = EffectiveValueBag()
        for fixedDiceValue in fixedDiceValues:
            dice = FixedDice(fixedDiceValue)
            bag.append(dice)

        result = bag.get_result()
        self.assertEqual(result, 6)
