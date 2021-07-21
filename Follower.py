from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest
from telethon.tl.types import InputPeerEmpty
import csv
from dotenv import dotenv_values

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

for chat in chats:
    try:
        with open('Followed.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            ids = []
            for row in reader:
                ids.append(int(row['id']))
            if chat.id not in ids:
                groups.append(chat)
    except:
        continue

print('Which Group Yow Want To Follow:')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1

g_index = input("Please! Enter a Number: ")
target_group=groups[int(g_index)]

print('Saving In file...')
with open("Followed.csv","a",encoding='UTF-8') as f:
    fieldnames = ['id', 'title']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow({'id': target_group.id, 'title': target_group.title})
print('Chat Followed successfully.......')
