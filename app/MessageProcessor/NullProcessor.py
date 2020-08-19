import discord
from . import AbstractProcessor

class NullProcessor(AbstractProcessor.AbstractProcessor):
    async def process(self, message: discord.Message):
        # 何もしないメソッドを呼び出せるようにしておく
        return
