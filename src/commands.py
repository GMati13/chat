import shlex
import lib.ui.body as body
import lib.ui.footer as footer
import lib.urwid as urwid
import sys
import src.handlers.client.chats as chat
from client import client
import src.storage as store

def send():
    chat_id = store.get_item('current_chat')['id']
    chat_type = store.get_item('current_chat')['type']
    if chat_id is None:
        return 'Error: chat has not selected'
    text = footer.message_line.get_edit_text()
    footer.message_line.clear()
    message = client.send_message(chat_id, text)
    chat.append_message(message, chat_type)
    body.history.scroll_end()

def exit():
    client.stop()
    sys.exit()

commands = {
    'q': lambda args: exit(),
    'quit': lambda args: exit(),
    's': lambda args: send(),
    'send': lambda args: send(),
    'dialogs': lambda args: chat.get_dialogs(),
}

def do_command(line):
    args = shlex.split(line)
    if args[0] in commands:
        return commands[args[0]](args[1:])
    return 'Error: unknown command \'{c}\''.format(c=args[0])
