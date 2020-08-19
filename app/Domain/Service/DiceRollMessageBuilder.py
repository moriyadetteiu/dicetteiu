import collections
from Domain.ValueObject.Dice import Dice

# 自身のクラスをタイプヒントできないらしいので、メソッドチェーンする場合は返り値のタイプヒントはしない
class DiceRollMessageBuilder:
    def __init__(self):
        self.__raw_content = None
        self.__dices = []
        self.__judge_results = []


    def set_raw_content(self, raw_content: str):
        self.__raw_content = raw_content
        return self

    # TODO: ここで補正値とかも受け取れるようにする
    def append_dice(self, dice: Dice):
        self.__dices.append(dice)
        return self

    def append_judge_result(self, judgeResult: str):
        self.__judge_results.append(judgeResult)
        return self

    def build(self) -> str:
        messages = []
        if self.__raw_content:
            messages.append(f'> {self.__raw_content}')

        dice_results = [str(dice.get_result()) for dice in self.__dices]
        dice_result_message = ', '.join(dice_results)
        messages.append(dice_result_message)

        if len(self.__judge_results) > 0:
            judge_result_aggregates = collections.Counter(self.__judge_results)
            for result, count in judge_result_aggregates.items():
                messages.append(f'{result}: {count}個')

        return '\n'.join(messages)
