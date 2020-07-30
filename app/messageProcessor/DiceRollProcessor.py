import re
import random
import discord
from . import AbstractProcessor

class DiceRollProcessor(AbstractProcessor.AbstractProcessor):
    async def process(self, message: discord.Message):
        content = message.content
        parsed_content = self.parse(content)

        results = []
        for i in range(parsed_content['number_of_dice']):
            result = random.randint(1, parsed_content['maximum_number'])
            results.append(str(result))

        responce_message = ', '.join(results)
        await message.channel.send(responce_message)

    def parse(self, content):
        result = re.match(r'^([0-9]+)d([0-9]+)', content)
        return {
            'number_of_dice': int(result.group(1)),
            'maximum_number': int(result.group(2))
        }
