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
import src.templates.store as store_template
from client import client

def get_chat(chat_id):
    body.history.clear()
    body.history.append_child(urwid.Text(str(client.get_chat(chat_id))))

def read_history(chat_id):
    api.messages.read_history(chat_id)

def append_message(message, chat_type):
    is_me = message['outgoing'] or store.get_item('me')['id'] == message['from_user']['id']
    if chat_type == 'private':
        body.history.append_child(urwid.AttrMap(
            urwid.Message(message),
            theme.green_light if is_me else theme.main_light,
            theme.green_dark if is_me else theme.main_dark
        ))
    elif chat_type in ['group', 'channel']:
        body.history.append_child(urwid.AttrMap(
            urwid.Message(message),
            theme.main_light,
            theme.main_dark
        ))

def select_chat(chat_id):
    body.history.clear()
    dialog = list(filter(
        lambda d: d['chat']['id'] == chat_id,
        store.get_item('dialogs')['dialogs']
    ))[0]
    app.mode.toggle_mode('chat')
    history = client.get_history(chat_id)
    store.set_item('current_chat', dialog['chat'])
    for message in history['messages'][::-1]:
        append_message(message, dialog['chat']['type'])
    body.history.scroll_end()

def show_dialog_info(position):
    dialog = store.get_item('dialogs')['dialogs'][position]
    if dialog['chat']['type'] == 'private':
        footer.info_line.left_column.set_text(status_line.info_dialog_private.format(
            username=dialog['chat']['username'] if dialog['chat']['username'] else 'no username',
            fullname=formatter.formate_name(dialog['chat']['first_name'], dialog['chat']['last_name']),
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
        if dialog['chat']['type'] in ['private', 'group', 'channel']:
            body.history.append_child(urwid.AttrMap(urwid.Dialog(dialog), theme.main_light, theme.main_dark))
        else:
            body.history.append_child(urwid.Text(status_line.info_unsupported_channel))

    header.Header.left_column.set_text(status_line.header_dialogs.format(
        total_count=dialogs['total_count']
    ))
    app.mode.toggle_mode('DIALOGS')
