import discord
from . import AbstractProcessor
from . import DiceRollProcessor

def generate(message: discord.Message) -> AbstractProcessor:
    return DiceRollProcessor.DiceRollProcessor()
