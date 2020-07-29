from abc import *
import discord

class AbstractProcessor(metaclass=ABCMeta):
    @abstractmethod
    def process(self, message: discord.Message):
        pass
