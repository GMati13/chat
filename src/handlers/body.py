import lib.ui.body as body
import lib.ui.footer as footer
import src.app as app
import src.keybins as keybins
import src.storage as store
import src.templates.statusline as status_line
import src.handlers.client.chats as chats

def history_on_key_press(key, List):
    if app.mode.current_mode == 'DIALOGS':
        if key in keybins.dialogs:
            return keybins.dialogs[key]() or key
    elif app.mode.current_mode == 'CHAT':
        if key in keybins.chat:
            return keybins.chat[key]() or key
    if key in ['enter']:
        return key

def history_on_after_key_press(key, List):
    if app.mode.current_mode == 'DIALOGS':
        try:
            chats.show_dialog_info(List.focus_position)
        except Exception:
            pass

def history_on_enter(position, List):
    if app.mode.current_mode == 'DIALOGS':
        chats.select_chat(store.get_item('dialogs')['dialogs'][position]['chat']['id'])

body.history.on_key_press = history_on_key_press
body.history.on_after_key_press = history_on_after_key_press
body.history.on_enter = history_on_enter
