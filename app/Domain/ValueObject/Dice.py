import random
from Domain.Exceptions.InvalidArgumentException import InvalidArgumentException

class Dice:
    def __init__(self, side: int):
        if side <= 0:
            raise InvalidArgumentException('ダイスは1面以上必要です')

        self.__side = side
        self.__roll_result = None

    def roll(self):
        self.__roll_result = random.randint(1, self.__side)
        return self.__roll_result

    def get_result(self):
        if self.__roll_result == None:
            raise RuntimeError('ダイスロールがされていません')

        return self.__roll_result
