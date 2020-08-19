from Domain.Entity.TargetLevelGettableInterface import TargetLevelGettableInterface

class TargetLevelBag(TargetLevelGettableInterface):
    def __init__(self):
        self.__targetLevels = []

    def append(self, targetLevel: TargetLevelGettableInterface):
        self.__effectiveValues.append(effectiveValue)

    # 一旦減算とかは考慮せず、加算のみで記述する
    def get_level(self) -> int:
        result = 0
        for targetLevel in self.__targetLevels:
            # calcuratableInterfaceを継承している場合のみ、メソッドに引き渡して処理させる？
            result = result + targetLevel.get_level()

        return result
