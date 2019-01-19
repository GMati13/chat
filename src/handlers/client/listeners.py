from client import client
import src.handlers.client.chats as chat
import src.storage as store
import lib.ui.body as body
import lib.urwid as urwid

@client.on_message()
def on_message(c, message):
    chat = store.get_item('current_chat')
    if chat is None:
        return
    chat_id = chat['id']
    chat_type = chat['type']
    if message['chat']['id'] == chat_id:
        chat.append_message(message, chat_type)
        body.history.scroll_end()
