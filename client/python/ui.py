from components import Window, TextInput, List, ListWalker, Divider, AttrMap, Text, Container, Filler, SolidFill, Message
from styles import palette
import styles as style

msg_list = List(auto_scroll='end')
msg_line = TextInput()

divider = AttrMap(Divider(), style.DIVIDER)

cmd_line = TextInput()

chat_status_line = divider
app_status_line = divider

header = None
body = msg_list
footer = Container([
    chat_status_line,
    msg_line,
    app_status_line,
    cmd_line
])

window = Window(body, footer=footer, focus_part='footer', palette=palette)
