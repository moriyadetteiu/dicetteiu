import re
import discord
from . import AbstractProcessor
from . import DiceRollProcessor
from . import NullProcessor

def generate(message: discord.Message) -> AbstractProcessor:
    content = message.content

    if re.match(r'^[0-9]+d[0-9]+', content):
        return DiceRollProcessor.DiceRollProcessor()

    return NullProcessor.NullProcessor()
