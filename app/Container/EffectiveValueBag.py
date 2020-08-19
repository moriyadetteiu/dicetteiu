from Domain.ValueObject.EffectiveValueGettableInterface import EffectiveValueGettableInterface

class EffectiveValueBag(EffectiveValueGettableInterface):
    def __init__(self):
        self.__effectiveValues = []

    def append(self, effectiveValue: EffectiveValueGettableInterface):
        self.__effectiveValues.append(effectiveValue)

    # 一旦減算とかは考慮せず、加算のみで記述する
    def get_result(self) -> int:
        result = 0
        for effectiveValue in self.__effectiveValues:
            # calcuratableInterfaceを継承している場合のみ、メソッドに引き渡して処理させる？
            result = result + effectiveValue.get_result()

        return result
