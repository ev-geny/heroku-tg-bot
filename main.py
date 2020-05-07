from telethon.sync import TelegramClient, events
# Вставляем api_id и api_hash
api_id = 1339341
api_hash = '6b0a952595f9c48d75400e3512b51872'

client = TelegramClient('session_name', api_id, api_hash)

client.start()
@client.on(events.NewMessage(chats=('statistika_baccara')))
async def normal_handler(event):
    messages= event.message.to_dict()['message']
    #if "#R" in messages and int(messages [2:6])%10==0:
    print(messages)
#print(event.message.to_dict()['message'])
    await client.send_message('statistika_baccara_bot', messages)


#messages =client.get_messages('statistika_baccara')
#messages =client.get_messages('zhe_b')
#print(messages[0].message)
#client.send_message('me', 'Hello to myself!')
client.run_until_disconnected()


