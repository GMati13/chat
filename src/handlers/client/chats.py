import lib.urwid as urwid
import lib.ui.body as body
import lib.ui.body as body
import lib.ui.footer as footer
import lib.ui.header as header
import src.templates.statusline as status_line
import src.storage as store
import src.app as app
import theme
import src.formatter as formatter
from client import client

def show_dialog_info(position):
    dialog = store.get_item('dialogs')['dialogs'][position]
    if dialog['chat']['type'] == 'private':
        user = client.get_users([dialog['chat']['id']])[0]
        footer.info_line.left_column.set_text(status_line.info_dialog_private.format(
            username=user['username'] if user['username'] else 'no username',
            fullname=formatter.formate_name(user['first_name'], user['last_name']),
            online=formatter.format_status(user['status'])
        ))
    elif dialog['chat']['type'] in ['group', 'channel']:
        footer.info_line.left_column.set_text(status_line.info_dialog_public.format(
            type=dialog['chat']['type'],
            title=dialog['chat']['title']
        ))
    else:
        footer.info_line.left_column.set_text(status_line.info_unsupported_channel)

def get_dialogs():
    header.Header.left_column.set_text(status_line.header_loading)
    body.history.clear()
    dialogs = client.get_dialogs()
    store.set_item('dialogs', dialogs)
    show_dialog_info(0)
    for dialog in dialogs['dialogs']:
        if dialog['chat']['type'] == 'private':
            body.history.append_child(urwid.AttrMap(urwid.Dialog(dialog), theme.main_light, theme.main_dark))
        elif dialog['chat']['type'] in ['group', 'channel']:
            body.history.append_child(urwid.AttrMap(urwid.Dialog(dialog), theme.main_light, theme.main_dark))
        else:
            body.history.append_child(urwid.Text(status_line.info_unsupported_channel))

    header.Header.left_column.set_text(status_line.header_dialogs.format(
        total_count=dialogs['total_count']
    ))
    app.mode.toggle_mode('DIALOGS')
