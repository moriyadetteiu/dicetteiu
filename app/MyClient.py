import discord
from messageProcessor.processor_generator import generate

class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        processor = generate(message)
        await processor.process(message)
        return
