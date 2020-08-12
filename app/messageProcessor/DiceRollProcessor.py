import collections
import re
import random
import discord
from . import AbstractProcessor
from Container import EnableChannelContainer
from Domain.ValueObject.Dice import Dice

class DiceRollProcessor(AbstractProcessor.AbstractProcessor):
    async def process(self, message: discord.Message):
        if not self.is_enable(message):
            return

        content = message.content
        parsed_content = self.parse(content)

        results = []
        compare_results = []
        for i in range(parsed_content['number_of_dice']):
            maximum_number = parsed_content['maximum_number']
            dice = Dice(maximum_number)
            result = dice.roll()
            modify_operator = parsed_content['result_modify_operator']
            modify_number = parsed_content['result_modify_number']
            modified_result = self.modify_roll_result(
                result,
                modify_operator,
                modify_number
            )
            modified_result_text = (
                f'({result}) {modify_operator} {modify_number} = {modified_result}'
                if result != modified_result
                else str(modified_result)
            )
            results.append(modified_result_text)
            compare_result = self.compare_result(
                maximum_number,
                modified_result,
                parsed_content['compare_method'],
                parsed_content['compare_number']
            )
            if compare_result != '':
                compare_results.append(compare_result)

        responce_message = ', '.join(results)
        compare_result_aggregates = collections.Counter(compare_results)
        compare_result_texts = []
        for result, count in compare_result_aggregates.items():
            compare_result_texts.append(f'{result}: {count}個')
        if len(compare_result_texts) > 0:
            responce_message += '\n' + '\n'.join(compare_result_texts)

        await message.channel.send(responce_message)

    def parse(self, content):
        result = re.match(r'^([0-9]+)d([0-9]+) *([+-/*/]*) *([0-9]*) *([><=]*) *([0-9]*)', content)
        return {
            'number_of_dice': int(result.group(1)),
            'maximum_number': int(result.group(2)),
            'result_modify_operator': result.group(3),
            'result_modify_number': result.group(4),
            'compare_method': result.group(5),
            'compare_number': result.group(6),
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

    def compare_result(self, maximum_number: int, result: int, method: str, number: str) -> str:
        if method == '' or number == '':
            return ''
        succeed = None
        number = int(number)
        if method == '>':
            succeed = result > number
        if method == '>=':
            succeed = result >= number
        if method == '<':
            succeed = result < number
        if method == '<=':
            succeed = result <= number
        if succeed == None:
            return ''
        return (
            (
                'クリティカル'
                if maximum_number == 100 and result <= 5
                else '成功'
            )
            if succeed
            else (
                'ファンブル'
                if maximum_number == 100 and result >= 95
                else '失敗'
            )
        )

    def is_enable(self, message: discord.Message):
        channel_id = int(message.channel.id)
        container = EnableChannelContainer.EnableChannelContainer()
        return container.is_enable_channel(channel_id)
