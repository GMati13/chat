from pyrogram import Client, api
import os

APP_PATH = os.environ['HOME'] + '/.vimgram'
SESSION_NAME = 'vimgram'
APP_ID = '403859'
APP_HASH = '118250775a656486d2bb61f85746168e'

if not os.path.exists(APP_PATH):
    os.makedirs(APP_PATH)

class VimgramClient(Client):
    def logout(self):
        self.send(api.functions.auth.LogOut())

client = Client(SESSION_NAME, api_id=APP_ID, api_hash=APP_HASH, workdir=APP_PATH)
