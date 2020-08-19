from Domain.ValueObject.EffectiveValueGettableInterface import EffectiveValueGettableInterface

class FixedDice(EffectiveValueGettableInterface):
    def __init__(self, fixedResult: int):
        self.result = fixedResult

    def get_result(self) -> int:
        return self.result
