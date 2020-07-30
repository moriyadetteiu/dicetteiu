import re
import discord
from . import AbstractProcessor
from . import MessageContentException
from Container import EnableChannelContainer

class ChannelSettingProcessor(AbstractProcessor.AbstractProcessor):
    async def process(self, message: discord.Message):
        content = message.content
        try:
            parsed_content = self.parse(content)

            channel = message.guild.get_channel(parsed_content['channel_id'])
            if channel == None:
                raise MessageContentException()

            container = EnableChannelContainer.EnableChannelContainer()
            if parsed_content['is_enable']:
                container.enable_channel_id(channel.id)
            else:
                container.disable_channel_id(channel.id)

            is_enable_message = '有効' if parsed_content['is_enable'] else '無効'
            responce_message = f'{channel.name}({channel.id})でのダイスボットを{is_enable_message}化しました。'
            await message.channel.send(responce_message)
        except:
            channels = [
                f'{channel.id}: {channel.name}'
                for channel in message.guild.text_channels
            ]
            responce_message = '\n'.join(channels)
            await message.channel.send(f'存在するチャンネルを指定してください。\n{responce_message}')

    def parse(self, content):
        is_enable = not bool(re.match(r'.*--disable.*', content))
        channel_id_result = re.match(r'/dicetteiu channel .*? ?([0-9]+)', content)
        if not bool(channel_id_result):
            raise MessageContentException()

        channel_id = int(channel_id_result.group(1))
        return {
            'is_enable': is_enable,
            'channel_id': channel_id
        }
