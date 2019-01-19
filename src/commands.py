import shlex
import lib.ui.body as body
import lib.ui.footer as footer
import lib.urwid as urwid
import sys
import src.handlers.client.chats as chats
from client import client

def send():
    body.history.append_child(urwid.Text(footer.message_line.edit_text))
    body.history.scroll_down()
    body.history.scroll_down()
    body.history.scroll_down()
    footer.message_line.clear()

def exit():
    client.stop()
    sys.exit()

commands = {
    'q': lambda args: exit(),
    'quit': lambda args: exit(),
    's': lambda args: send(),
    'send': lambda args: send(),
    'dialogs': lambda args: chats.get_dialogs(),
}

def do_command(line):
    args = shlex.split(line)
    if args[0] in commands:
        return commands[args[0]](args[1:])
    return 'Error: unknown command \'{c}\''.format(c=args[0])
