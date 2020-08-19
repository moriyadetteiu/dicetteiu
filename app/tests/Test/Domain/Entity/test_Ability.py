from unittest import TestCase
from Domain.Entity.Ability import Ability
from Domain.Exceptions.InvalidArgumentException import InvalidArgumentException

class TestAbility(TestCase):
    def test_init(self):
        ability = Ability('test')

        with self.assertRaises(InvalidArgumentException):
            unavailable_ability = Ability('')

    def test_get_name(self):
        NAME = 'test'
        ability = Ability(NAME)
        self.assertEqual(ability.get_name(), NAME)
