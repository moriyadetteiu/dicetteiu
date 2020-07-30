from . import Singleton

class EnableChannelContainer(Singleton.Singleton):
    def __init__(self):
        if not hasattr(self, '_channel_ids'):
            self._channel_ids = set([])

    def enable_channel_id(self, channel_id: int):
        self._channel_ids.add(channel_id)

    def disable_channel_id(self, channel_id: int):
        self._channel_ids.discard(channel_id)

    def is_enable_channel(self, channel_id: int):
        return channel_id in self._channel_ids
