from unittest import TestCase
from Domain.ValueObject.Dice import Dice
from Domain.Exceptions.InvalidArgumentException import InvalidArgumentException

class TestDice(TestCase):
    def test_init(self):
        # 普通にインスタンス化できることの確認
        dice = Dice(5)

        with self.assertRaises(InvalidArgumentException):
            dice = Dice(0)

        with self.assertRaises(InvalidArgumentException):
            dice = Dice(-5)

    def test_roll(self):
        SIDE = 10
        dice = Dice(SIDE)

        # ダイスロールをせずに結果を取得した場合、例外が飛ぶはず
        with self.assertRaises(RuntimeError):
            dice.get_result()

        result = dice.roll()
        self.assertGreater(result, 0)
        self.assertLessEqual(result, SIDE)
        self.assertEqual(result, dice.get_result())
