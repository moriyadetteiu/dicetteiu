import re
import random
import discord
from . import AbstractProcessor
from Container import EnableChannelContainer

class DiceRollProcessor(AbstractProcessor.AbstractProcessor):
    async def process(self, message: discord.Message):
        if not self.is_enable(message):
            return

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

    def is_enable(self, message: discord.Message):
        channel_id = int(message.channel.id)
        container = EnableChannelContainer.EnableChannelContainer()
        return container.is_enable_channel(channel_id)
