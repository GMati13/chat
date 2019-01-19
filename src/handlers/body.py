import lib.ui.body as body
import src.app as app
import src.keybins as keybins
import src.storage as store
import src.templates.statusline as status_line
from src.handlers.client.chats import show_dialog_info

def history_on_key_press(key, List):
    if app.mode.current_mode == 'DIALOGS':
        if key in keybins.dialogs:
            return keybins.dialogs[key]()
        
def history_on_after_key_press(key, List):
    if app.mode.current_mode == 'DIALOGS':
        show_dialog_info(List.focus_position)

body.history.on_key_press = history_on_key_press
body.history.on_after_key_press = history_on_after_key_press
