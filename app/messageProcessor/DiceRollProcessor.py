import re
import random
import discord
from . import AbstractProcessor
from Container import EnableChannelContainer

class DiceRollProcessor(AbstractProcessor.AbstractProcessor):
    async def process(self, message: discord.Message):
        if not self.is_enable(message) and False:
            return

        content = message.content
        parsed_content = self.parse(content)

        results = []
        for i in range(parsed_content['number_of_dice']):
            result = random.randint(1, parsed_content['maximum_number'])
            modify_operator = parsed_content['result_modify_operator']
            modify_number = parsed_content['result_modify_number']
            modified_result = self.modify_roll_result(
                result,
                modify_operator,
                modify_number
            )
            if result != modified_result:
                modified_result = f'({result}) {modify_operator} {modify_number} = {modified_result}'
            results.append(str(modified_result))

        responce_message = ', '.join(results)
        await message.channel.send(responce_message)

    def parse(self, content):
        result = re.match(r'^([0-9]+)d([0-9]+) *([+-/*/]*) *([0-9]*)', content)
        return {
            'number_of_dice': int(result.group(1)),
            'maximum_number': int(result.group(2)),
            'result_modify_operator': result.group(3),
            'result_modify_number': result.group(4),
        }

    def modify_roll_result(self, result: int, operator: str, number: str) -> int:
        if operator == '' or number == '':
            return result
        number = int(number)
        if operator == '+':
            return result + number
        if operator == '-':
            return result - number
        if operator == '*':
            return result * number
        if operator == '/':
            return result / number

    def is_enable(self, message: discord.Message):
        channel_id = int(message.channel.id)
        container = EnableChannelContainer.EnableChannelContainer()
        return container.is_enable_channel(channel_id)
