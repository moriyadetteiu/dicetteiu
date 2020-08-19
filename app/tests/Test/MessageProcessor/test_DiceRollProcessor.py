import random
import unittest
from MessageProcessor.DiceRollProcessor import DiceRollProcessor

class TestDiceRollProcessor(unittest.TestCase):
    def test_build_message_simple(self):
        processor = DiceRollProcessor()
        message = processor.build_message('1d1')
        self.assertEqual(message, '> 1d1\n1')

    def test_build_message_judge(self):
        processor = DiceRollProcessor()

        # 結果を固定するために、シード値をまく
        random.seed(1)
        message = processor.build_message('1d100')
        self.assertEqual(message, '> 1d100\n18')

        random.seed(1)
        message = processor.build_message('1d100 < 50')
        self.assertEqual(message, '> 1d100 < 50\n18\n成功: 1個')

        random.seed(1)
        message = processor.build_message('1d100 < 10')
        self.assertEqual(message, '> 1d100 < 10\n18\n失敗: 1個')

        random.seed(23)
        message = processor.build_message('1d100 < 50')
        self.assertEqual(message, '> 1d100 < 50\n100\nファンブル: 1個')

        random.seed(31)
        message = processor.build_message('1d100 < 50')
        self.assertEqual(message, '> 1d100 < 50\n2\nクリティカル: 1個')

    @unittest.skip('複数ダイス、補正値を実装した後に有効化する')
    def test_build_message_multi(self):
        processor = DiceRollProcessor()

        # 結果を固定するために、シード値をまく
        random.seed(1)
        message = processor.build_message('1d3 + 1d4')
        self.assertEqual(message, '> 1d3 + 1d4...')
