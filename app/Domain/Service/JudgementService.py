from Domain.Entity.TargetLevelGettableInterface import TargetLevelGettableInterface
from Domain.ValueObject.EffectiveValueGettableInterface import EffectiveValueGettableInterface
from .Comparator.comparator_generator import generate
from .Comparator.NullComparator import NullComparator

class JudgementService:
    def judge(self, dice: EffectiveValueGettableInterface, ownedAbility: TargetLevelGettableInterface, method: str):
        comparator = generate(method)
        criticalConparator = generate('<=')
        fumbleConparator = generate('>')

        isSucceed = comparator.compare(dice, ownedAbility)
        isCritical = isSucceed and dice.get_result() <= 5
        isFumble = not isSucceed and dice.get_result() > 95

        # 文字列で返しているけど、それぞれラップしたオブジェクトで返すべき？
        if isCritical:
            return 'クリティカル'
        elif isFumble:
            return 'ファンブル'
        elif isSucceed:
            return '成功'
        else:
            return '失敗'

    # 数字かどうかここで判断するのは微妙かも？（一旦仮置き）
    # リクエスト周りなので、もっとシステムよりの場所な気もする
    # パーサーに置く？
    def is_judgeable(self, targetValueStr: str, method: str) -> bool:
        comparator = generate(method)
        isDecimalValue = targetValueStr.isdecimal()
        isComparatableMethod = not isinstance(comparator, NullComparator)
        return isDecimalValue and isComparatableMethod
