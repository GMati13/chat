from components import Window, TextInput, List, ListWalker, Divider, AttrMap, Text, Container, Filler, SolidFill, Message, StatusLine
from styles import palette
import styles as style

msg_list = List(auto_scroll='end')
msg_line = TextInput()

divider = AttrMap(Divider(), style.DIVIDER)

cmd_line = TextInput()

chat_status_line = StatusLine()
app_status_line = StatusLine()

header = None
body = msg_list
footer = Container([
    chat_status_line,
    msg_line,
    app_status_line,
    cmd_line
])

NORMAL_MODE = 'normal'
MESSAGE_MODE = 'message'
COMMAND_MODE = 'command'
CURRENT_MODE = ''

def toggle_mode(mode):
    global NORMAL_MODE, MESSAGE_MODE, COMMAND_MODE, CURRENT_MODE, window, msg_line, cmd_line, app_status_line

    if mode not in [NORMAL_MODE, COMMAND_MODE, MESSAGE_MODE]:
        return
    if mode in [NORMAL_MODE, MESSAGE_MODE]:
        window.document.set_focus('footer')
        window.footer.set_focus(msg_line)
        cmd_line.set_caption('')
    elif mode == COMMAND_MODE:
        window.document.set_focus('footer')
        window.footer.set_focus(cmd_line)
        cmd_line.set_caption(':')
    cmd_line.edit_text = ''
    app_status_line.left_column.set_text('['+mode+']')
    CURRENT_MODE = mode

window = Window(body, footer=footer, focus_part='footer', palette=palette)

toggle_mode(NORMAL_MODE)
