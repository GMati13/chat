from pyrogram import Client, api
import os

APP_DIR = os.path.join(os.environ['HOME'], '.vimgram')
SESSION_NAME = 'vimgram'
APP_ID = '403859'
APP_HASH = '118250775a656486d2bb61f85746168e'
SESSION_FILE = os.path.join(APP_DIR, '{s}.session'.format(s=SESSION_NAME))

class VimgramClient(Client):
    def logout(self):
        self.send(api.functions.auth.LogOut())
        os.remove(SESSION_FILE) if os.path.exists(SESSION_FILE) else None

client = VimgramClient(SESSION_NAME, api_id=APP_ID, api_hash=APP_HASH, workdir=APP_DIR)
