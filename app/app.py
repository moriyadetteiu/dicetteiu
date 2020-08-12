import os
import sys
import MyClient

from Domain.ValueObject.Dice import Dice
dice = Dice(1)
print("1")
sys.exit()
print("2")

try:
    token = os.environ['DICE_BOT_TOKEN']
except KeyError:
    print('環境変数「DICE_BOT_TOKEN」を設定してください')
    sys.exit()

client = MyClient.MyClient()
client.run(token)
