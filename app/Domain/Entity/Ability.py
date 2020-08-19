from Domain.Exceptions.InvalidArgumentException import InvalidArgumentException

class Ability():
    def __init__(self, name: str):
        if len(name) == 0:
            raise InvalidArgumentException('技能名は1文字以上にしてください')

        self.__name = name

    def get_name(self) -> str:
        return self.__name
