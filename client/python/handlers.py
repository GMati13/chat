import urwid
import ui
import command as cmd
from client import client

@client.on_message()
def client_on_message(c, message):
    if message['chat']['type'] == client.PRIVATE:
        if message['chat']['username'] == client.CHAT_WITH['username']:
            ui.msg_list.append_child(ui.Message(message))

@client.on_user_status()
def on_user_status(c, data):
    if data['user_id'] == client.CHAT_WITH['id']:
        client.update_chat_with()

def msg_line_on_enter(value):
    message = client.send_message(client.CHAT_WITH['username'], value)
    ui.msg_list.append_child(ui.Message(message, text=value))
    return 0

motion = { 'h': 'left', 'j': 'down', 'k': 'left', 'l': 'right' }

def msg_line_on_key_press(size, key):
    if ui.CURRENT_MODE == ui.NORMAL_MODE:
        if key == cmd.command_sign: ui.toggle_mode(ui.COMMAND_MODE)
        elif key == 'i': ui.toggle_mode(ui.MESSAGE_MODE)
        elif key in ['h', 'j', 'k', 'l']: return motion[key]
        return None
    elif ui.CURRENT_MODE == ui.MESSAGE_MODE:
        if key == 'esc': ui.toggle_mode(ui.NORMAL_MODE)
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
        client.chat_with(tail)
    ui.toggle_mode(ui.NORMAL_MODE)
    return 0

def cmd_line_on_key_press(size, key):
    if key == 'esc': ui.toggle_mode(ui.NORMAL_MODE)
    return key
