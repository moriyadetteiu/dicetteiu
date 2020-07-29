import discord
from . import AbstractProcessor

class DiceRollProcessor(AbstractProcessor.AbstractProcessor):
    def process(self, message: discord.Message):
        print('ok')
