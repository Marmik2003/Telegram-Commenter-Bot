from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest
from telegram.ext.dispatcher import run_async
from telethon.tl.types import InputPeerEmpty
import csv
import telebot
from dotenv import dotenv_values
import asyncio
import time

bot = telebot.AsyncTeleBot(dotenv_values('.env')['API_KEY']) 

api_id = int(dotenv_values('.env')['user_id']) 
api_hash = dotenv_values('.env')['user_hash']
phone = dotenv_values('.env')['user_phone']

client = TelegramClient(phone, api_id, api_hash)
async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello !!!!')
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter verification code: '))


chats = []
last_date = None
chunk_size = 200
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

with open('Followed.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    ids = []
    messages_to_send = []
    for row in reader:
        ids.append(int(row['id']))
    for chat in chats:
        if chat.id in ids:
            chat_messages = []
            posts = client(GetHistoryRequest(
                peer=chat,
                limit=1,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0))
            chat_title = chat.title
            for msg in posts.messages:
                message = chat_title + ' - ' + str(msg.date) + '\n' + msg.message
                chat_messages.append(message)
            messages_to_send.append(chat_messages)

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, 'Hey, This is message commenter bot! have you run the Follower python script, then you can get messages by command /getMessage , Thank you.')


@bot.message_handler(commands=['getMessage'])
def send_commentings(message):
    for chat in messages_to_send:
        for msg in chat:
            bot.send_message(message.chat.id, msg)

bot.polling()