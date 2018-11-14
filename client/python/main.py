import ui
import command
import wsclient
import action
from urwid import Text

app = ui.Window(vertical_align='bottom')

def on_message(ws, message): msg_container.append_child(Text(message))

client = wsclient.WSClient(on_message=on_message)

msg_container = ui.Container()

def on_enter(value):
    if command.has_true(value):
        cmd = command.pretty(value)
        if   cmd['head'] in ('q', 'quit', 'exit'):    action.exit_from_app(app, client)
        elif cmd['head'] in ('c', 'conn', 'connect'): action.run_socket_connection(client, cmd['args'][0])
        return 0
    if client.socket != None:
        client.socket.send(value)
    return 0

msg_input = ui.TextInput('message: ', on_enter=on_enter)

for item in (msg_container, msg_input): app.body.append_child(item)

app.body.set_focus(msg_input)

app.run()
