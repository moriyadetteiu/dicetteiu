import pickle
import os
from . import Singleton

FOREVER_FILE_PATH = '/tmp/app/enableChannelIds.pkl'

class EnableChannelContainer(Singleton.Singleton):
    def __init__(self):
        if not hasattr(self, '_channel_ids'):
            if os.path.isfile(FOREVER_FILE_PATH):
                with open(FOREVER_FILE_PATH, 'rb') as f:
                    self._channel_ids = pickle.load(f)
            else:
                self._channel_ids = set([])

    def enable_channel_id(self, channel_id: int):
        self._channel_ids.add(channel_id)
        self.forever_channel_ids()

    def disable_channel_id(self, channel_id: int):
        self._channel_ids.discard(channel_id)
        self.forever_channel_ids()

    def forever_channel_ids(self):
        with open(FOREVER_FILE_PATH, 'wb') as f:
            pickle.dump(self._channel_ids, f)

    def is_enable_channel(self, channel_id: int):
        return channel_id in self._channel_ids
