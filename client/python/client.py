from pyrogram import Client, api
import ui
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
    CHAT_WITH = None

    def logout(self):
        self.send(api.functions.auth.LogOut())
        os.remove(SESSION_FILE) if os.path.exists(SESSION_FILE) else None

    def update_chat_with(self):
        self.CHAT_WITH = self.get_me() if self.CHAT_WITH['is_self'] is True else self.get_users(self.CHAT_WITH['id'])
        self.update_status_line()

    def chat_with(self, id):
        self.CHAT_WITH = self.get_me() if id is 'me' else self.get_users(id)
        history = self.get_history(self.CHAT_WITH['username'])
        ui.msg_list.body = ui.ListWalker([])
        for message in history['messages'][::-1]:
            ui.msg_list.append_child(ui.Message(message))
        self.update_status_line()

    def update_status_line(self):
        f_name = self.CHAT_WITH['first_name']
        l_name = self.CHAT_WITH['last_name'] if self.CHAT_WITH['last_name'] else ''
        ui.chat_status_line.left_column.set_text(
            '['+('online' if self.CHAT_WITH['status']['online'] is True else 'offline')+'] '+
            (f_name if isinstance(f_name, str) else f_name.encode('utf-8')) + ' ' +
            (l_name if isinstance(l_name, str) else l_name.encode('utf-8'))
        )


client = VimgramClient(SESSION_NAME, api_id=APP_ID, api_hash=APP_HASH, workdir=APP_PATH)
