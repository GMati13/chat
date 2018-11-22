import urwid
import ui
import command as cmd
from client import client

@client.on_message()
def client_on_message(c, message):
    if message['chat']['type'] == client.PRIVATE:
        if message['chat']['username'] == client.chat_with:
            if message['from_user']['username'] == client.chat_with:
                ui.msg_list.append_child(ui.Message(message))
            else:
                ui.msg_list.append_child(ui.Message(text=message['text']))

def set_mode(mode_name):
    if mode_name not in ['normal', 'message', 'command']:
        return
    if mode_name == 'command':
        ui.cmd_line.set_caption(':')
        ui.footer.set_focus(ui.cmd_line)
    elif mode_name == 'message':
        ui.cmd_line.set_caption('')
        ui.footer.set_focus(ui.msg_line)
    elif mode_name == 'normal':
        ui.cmd_line.set_caption('')
        ui.footer.set_focus(ui.msg_line)
    client.mode = mode_name

def msg_line_on_enter(value):
    message = ui.Message(text=value)
    ui.msg_list.append_child(message)
    client.send_message(client.chat_with, value)
    return 0

motion = { 'h': 'left', 'j': 'down', 'k': 'left', 'l': 'right' }

def msg_line_on_key_press(size, key):
    if client.mode == 'normal':
        if key == cmd.command_sign: set_mode('command')
        elif key == 'i': set_mode('message')
        elif key in ['h', 'j', 'k', 'l']: return motion[key]
        return None
    elif client.mode == 'message':
        if key == 'esc': set_mode('normal')
        return key
    return None

def cmd_line_on_enter(value):
    command = value.strip().split(' ')
    head = command[0]
    tail = ' '.join(command[1:])
    if value in ['q', 'quit', 'exit']:
        client.stop()
        ui.window.exit()
    elif head in ['cw', 'chat', 'chatwith']:
        client.chat_with = tail
    set_mode('normal')
    return 0

def cmd_line_on_key_press(size, key):
    if key == 'esc': set_mode('normal')
    return key
