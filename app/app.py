import os
import sys
import MyClient

try:
    token = os.environ['DICE_BOT_TOKEN']
except KeyError:
    print('環境変数「DICE_BOT_TOKEN」を設定してください')
    sys.exit()

client = MyClient.MyClient()
client.run(token)
