from client import client
import src.handlers.client.chats as chat
import src.storage as store
import lib.ui.body as body
import lib.urwid as urwid

@client.on_message()
def on_message(c, message):
    current_chat = store.get_item('current_chat')
    if current_chat is None:
        return
    chat_id = current_chat['id']
    chat_type = current_chat['type']
    if message['chat']['id'] == chat_id:
        chat.append_message(message, chat_type)
        body.history.scroll_end()
