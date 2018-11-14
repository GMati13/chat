import ui
import command
import wsclient
import action
import urwid

palette = [
        ('msg input', '', 'black')
        ]

app = ui.Window(palette=palette, vertical_align='bottom')

def on_message(ws, message): msg_container.append_child(urwid.Text(message))

client = wsclient.WSClient(on_message=on_message)

msg_container = ui.Container()

def on_enter(value):
    if client.socket != None:
        client.socket.send(value)
    return 0

def on_key_press(size, key):
    if key == command.command_sign:
        cmd_input.set_caption(':')
        msg_input.set_caption('')
        app.body.set_focus(cmd_input_styled)
        return ''
    return key

def on_cmd_enter(value):
    cmd = command.pretty(value)
    if   cmd['head'] in command.exit:    action.exit_from_app(app, client)
    elif cmd['head'] in command.connect: action.run_socket_connection(client, cmd['tail'])
    cmd_input.set_caption('')
    msg_input.set_caption('> ')
    app.body.set_focus(msg_input_styled)
    return 0

def on_esc(value):
    cmd_input.set_caption('')
    msg_input.set_caption('> ')
    app.body.set_focus(msg_input_styled)
    return 0

msg_input = ui.TextInput(on_enter=on_enter, on_key_press=on_key_press)
msg_input_styled = urwid.AttrMap(msg_input, 'msg input')

cmd_input = ui.TextInput(on_enter=on_cmd_enter, on_esc=on_esc)
cmd_input_styled = urwid.AttrMap(cmd_input, 'cmd input')

divider = urwid.Divider()

for item in (msg_container, divider, msg_input_styled, cmd_input_styled): app.body.append_child(item)

msg_input.set_caption('> ')
app.body.set_focus(msg_input_styled)

app.run()
