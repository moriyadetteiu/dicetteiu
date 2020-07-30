from abc import *
import discord

class AbstractProcessor(metaclass=ABCMeta):
    @abstractmethod
    async def process(self, message: discord.Message):
        pass
