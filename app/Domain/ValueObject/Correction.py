from .EffectiveValueGettableInterface import EffectiveValueGettableInterface

class Correction(EffectiveValueGettableInterface):
    # operatorはinterfaceで受け取る形のがいいかも？
    def __init__(self, value: int, operator: str):
        self.__value = value

        # とりあえず後から使える形にしておく
        self.__operator = operator

    def get_result(self) -> int:
        return self.__value
