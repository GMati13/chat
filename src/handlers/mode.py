import lib.ui.footer as footer
import lib.ui.document as document
import lib.ui.body as body
import lib.urwid as urwid
import src.app as app
import src.templates.statusline as status_line
import src.storage as store
import src.formatter as formatter
from client import client

def on_init(mode):
    me = client.get_me()
    store.set_item('me', me)
    footer.status_line.left_column.set_text(status_line.app_status_left.format(
        mode=mode,
        username=formatter.formate_name(me['first_name'], me['last_name']),
        online=formatter.format_status(me['status'])
    ))
    body.history.append_child(urwid.Text(str(me)))

def on_toggle(prev_mode, next_mode):
    me = store.get_item('me')
    footer.status_line.left_column.set_text(status_line.app_status_left.format(
        mode=next_mode,
        username=formatter.formate_name(me['first_name'], me['last_name']),
        online=formatter.format_status(me['status'])
    ))
    if prev_mode in ['COMMAND']:
        footer.command_line.set_caption('')
    if next_mode in ['MESSAGE', 'NORMAL']:
        document.Document.set_focus('footer')
        footer.tools.set_focus(0)
        if prev_mode == 'COMMAND':
            footer.tools.set_focus(0)
    if next_mode in ['COMMAND']:
        document.Document.set_focus('footer')
        footer.tools.set_focus(2)
        footer.command_line.clear()
        footer.command_line.set_caption(':')
    if next_mode in ['DIALOGS', 'CHAT']:
        document.Document.set_focus('body')
    if next_mode in ['CHAT']:
        document.Document.set_focus('body')

app.mode.on_init = on_init
app.mode.on_toggle = on_toggle
