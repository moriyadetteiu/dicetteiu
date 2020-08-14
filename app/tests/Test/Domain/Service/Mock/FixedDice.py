from Domain.ValueObject.RollGettableInterface import RollGettableInterface

class FixedDice(RollGettableInterface):
    def __init__(self, fixedResult: int):
        self.result = fixedResult

    def get_result(self) -> int:
        return self.result
