from pyrogram import Client, api
import os

APP_PATH = os.environ['HOME'] + '/.vimgram'
SESSION_NAME = 'vimgram'
APP_ID = '403859'
APP_HASH = '118250775a656486d2bb61f85746168e'
SESSION_FILE = APP_PATH + '/' + SESSION_NAME + '.session'

if not os.path.exists(APP_PATH):
    os.makedirs(APP_PATH)

class VimgramClient(Client):
    PRIVATE = 'private'
    chat_with = None
    mode = 'normal'

    def logout(self):
        self.send(api.functions.auth.LogOut())
        os.remove(SESSION_FILE) if os.path.exists(SESSION_FILE) else None
        

client = VimgramClient(SESSION_NAME, api_id=APP_ID, api_hash=APP_HASH, workdir=APP_PATH)
