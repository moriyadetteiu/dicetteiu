import re
import discord
from . import AbstractProcessor
from Container import EnableChannelContainer
from Container.EffectiveValueBag import EffectiveValueBag
from Domain.Entity.Ability import Ability
from Domain.Entity.OwnedAbility import OwnedAbility
from Domain.Service.JudgementService import JudgementService
from Domain.Service.DiceRollMessageBuilder import DiceRollMessageBuilder
from Domain.ValueObject.Dice import Dice
from Domain.ValueObject.Correction import Correction

class DiceRollProcessor(AbstractProcessor.AbstractProcessor):
    async def process(self, message: discord.Message):
        if not self.is_enable(message):
            return

        content = message.content
        responce_message = self.build_message(content)
        await message.channel.send(responce_message)

    def build_message(self, content: str):
        parsed_content = self.parse(content)

        message_builder = DiceRollMessageBuilder()
        message_builder.set_raw_content(content)
        results = []
        compare_results = []
        for i in range(parsed_content['number_of_dice']):
            maximum_number = parsed_content['maximum_number']
            modify_operator = parsed_content['result_modify_operator']
            modify_number = parsed_content['result_modify_number']

            bag = EffectiveValueBag()
            dice = Dice(maximum_number)
            bag.append(dice)
            message_builder.append_dice(dice)
            result = dice.roll()

            # 後でここら辺はスマートにする。generator用意する感じ？
            if not (modify_operator == '' or modify_number == ''):
                correction = Correction(modify_number, modify_operator)
                bag.append(correction)

            judgement_service = JudgementService()
            compare_number = parsed_content['compare_number']
            compare_method = parsed_content['compare_method']
            if judgement_service.is_judgeable(compare_number, compare_method):
                level = int(compare_number)

                # 後々ステータスの自動読み取りなどをしたいので、ダミーでおいておく
                ability = Ability('any')
                owned_ability = OwnedAbility(ability, level)
                judge_result = judgement_service.judge(bag, owned_ability, compare_method)
                message_builder.append_judge_result(judge_result)

        return message_builder.build()

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

    def is_enable(self, message: discord.Message):
        channel_id = int(message.channel.id)
        container = EnableChannelContainer.EnableChannelContainer()
        return container.is_enable_channel(channel_id)
