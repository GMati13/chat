from client import client
import src.handlers.client.chats as chat
import src.storage as store
import lib.ui.body as body
import lib.urwid as urwid

@client.on_message()
def on_message(c, message):
    chat_id = store.get_item('current_chat')['id']
    chat_type = store.get_item('current_chat')['type']
    if message['chat']['id'] == chat_id:
        chat.append_message(message, chat_type)
        body.history.scroll_end()
