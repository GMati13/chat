import ui
import command
import wsclient
import action
import urwid
import locale
import time
import keybind
from threading import Thread
from datetime import datetime
import subprocess as s
import json

locale.setlocale(locale.LC_ALL, 'en_US.utf8')

palette = [
        ('status bar', '', 'black'),
        ('author', '', 'black')
        ]

app = ui.Window(palette=palette, vertical_align='bottom')

cmd_input_sign = ':'
msg_input_sign = ''

def toggle_win_mode(mode):
    if mode in ('msg', 'message', 'ml', 'multiline'):
        cmd_input.edit_text = ''
        cmd_input.set_caption('')
        msg_input.set_caption(msg_input_sign)
        if mode in ('ml', 'multiline'): win_mode.set_text('[multiline message]')
        else:                           win_mode.set_text('[message]')
        app.body.set_focus(msg_input_styled)
    elif mode in ('cmd', 'command'):
        cmd_input.set_caption(cmd_input_sign)
        win_mode.set_text('[command]')
        app.body.set_focus(cmd_input_styled)
    elif mode in ('nrm', 'normal'):
        cmd_input.set_caption('')
        cmd_input.edit_text = ''
        win_mode.set_text('[normal]')
        app.body.set_focus(msg_input_styled)

def on_message(ws, data):
    msg = json.loads(data)
    msg_container.append_child(ui.message(msg['text'], msg['author']))
    if msg['author'] != user_name.text:
        s.call(['notify-send', 'vimchat' , msg['author'] + ':\n' + msg['text']])

client = wsclient.WSClient(on_message=on_message)

msg_container = ui.Container()

def on_enter(value):
    if win_mode.text != '[multiline message]':
        action.send_message(client, value[:-1], user_name.text)
        return 0

def on_key_press(size, key):
    if win_mode.text == '[normal]':
        if key == command.command_sign:
            toggle_win_mode('command')
        if key == 'i': toggle_win_mode('message')
        if key in keybind.keys:
            return keybind.keys[key]
        return ''
    return key

def on_esc(value):
    toggle_win_mode('normal')

def on_cmd_enter(value):
    cmd = command.pretty(value)
    if   cmd['head'] in command.exit:
        action.exit_from_app(app, client)
        real_time_thread._stop()
    elif cmd['head'] in command.connect and cmd['tail']:
        action.run_socket_connection(client, cmd['tail'])
    elif cmd['head'] in command.send_message:
        action.send_message(client, msg_input.edit_text, user_name.text)
        msg_input.edit_text = ''
    elif cmd['head'] in command.set_name and cmd['tail']:
        user_name.set_text(cmd['tail'])
    elif cmd['head'] in command.multiline:
        toggle_win_mode('multiline')
        return 0
    toggle_win_mode('normal')
    return 0

def on_cmd_esc(value):
    toggle_win_mode('normal')
    return 0

msg_input = ui.TextInput(multiline=True, on_enter=on_enter, on_key_press=on_key_press, on_esc=on_esc)
msg_input_styled = urwid.AttrMap(msg_input, 'msg input')

cmd_input = ui.TextInput(on_enter=on_cmd_enter, on_esc=on_cmd_esc)
cmd_input_styled = urwid.AttrMap(cmd_input, 'cmd input')

user_name = urwid.Text('No name', align='right')

status_bar = urwid.Columns([
    user_name
    ])
status_bar_styled = urwid.AttrMap(status_bar, 'status bar')

win_mode = urwid.Text('')
real_time = urwid.Text('time zone', align='right')

def update_real_time():
    while True:
        real_time.set_text(str(datetime.now().strftime('%a %b %d %H:%M:%S')))
        time.sleep(1)
real_time_thread = Thread(target=update_real_time)
real_time_thread.daemon = True
real_time_thread.start()

cmd_status_bar = urwid.Columns([
    win_mode,
    real_time
    ])
cmd_status_bar_styled = urwid.AttrMap(cmd_status_bar, 'status bar')

msg_box = urwid.AttrMap(msg_container, 'msg box')

for item in (msg_box, status_bar_styled, msg_input_styled, cmd_status_bar_styled, cmd_input_styled): app.body.append_child(item)

toggle_win_mode('normal')

app.run()
