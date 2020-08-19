from unittest import TestCase
from Domain.Entity.Ability import Ability
from Domain.Entity.OwnedAbility import OwnedAbility
from Domain.Exceptions.InvalidArgumentException import InvalidArgumentException

class TestOwnedAbility(TestCase):
    def test_init(self):
        ability = Ability('test')
        ownedAbility = OwnedAbility(ability, 0)
        ownedAbility = OwnedAbility(ability, 100)

        with self.assertRaises(InvalidArgumentException):
            ownedAbility = OwnedAbility(ability, -1)

        with self.assertRaises(InvalidArgumentException):
            ownedAbility = OwnedAbility(ability, 101)

    def test_get_level(self):
        LEVEL = 50
        ability = Ability('test')
        ownedAbility = OwnedAbility(ability, LEVEL)
        self.assertEqual(ownedAbility.get_level(), LEVEL)
