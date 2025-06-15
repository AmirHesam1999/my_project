#!/bin/python3

from telethon.sync import TelegramClient

def orfile(i):
    with open("/home/hesam/Documents/Hesam/my_project/telegram-app/read_message/file.txt", "r") as f:
        s = f.readlines()
    
    
    if len(s)-1 == i:
        return s[i]
    else:
        return s[i][0:-1]
# Replace these with your own values
api_id = 21205632      # Your API ID
api_hash = 'fa18809980a7cb20f1114f7d4c6ade64'  # Your API Hash
channel_username = orfile(0)  # or 'https://t.me/channelusername'

# Create the client
client = TelegramClient('session_name', api_id, api_hash)

with client:
    for message in client.iter_messages(channel_username, limit=10):
        print(f"{message.sender_id}: {message.text}")