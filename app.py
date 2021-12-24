import json
import os

from telegram.ext import Updater


BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

tg = Updater(token=BOT_TOKEN)


def send_message_to_telegram(event: dict, context: dict):
    tg.bot.send_message(CHAT_ID, event['body'])
    return {'body': '', 'statusCode': 200}


def test(event: dict, context: dict):
    return {'body': json.dumps(event), 'statusCode': 200}
