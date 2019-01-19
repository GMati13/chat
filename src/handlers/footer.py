import lib.ui.body as body
import lib.urwid as urwid
import lib.ui.footer as footer
import src.keybins as keybins
import src.app as app
import src.commands as command

def message_line_on_enter(value, Edit):
    command.send()

def message_line_on_key_press(key, Edit):
    if app.mode.current_mode == 'NORMAL':
        if key in keybins.normal:
            return keybins.normal[key]()
        return None
    if app.mode.current_mode == 'MESSAGE':
        if key in keybins.message:
            return keybins.message[key]() or key
    return key

def message_line_on_click(event, button, x, y, focus):
    app.mode.toggle_mode('normal')
    body.history.clear()

def command_line_on_enter(value, Edit):
    result = command.do_command(value)
    if result is not None:
        Edit.set_edit_text(str(result))
    if app.mode.current_mode == 'COMMAND':
        app.mode.toggle_mode(app.mode.previous_mode)

def command_line_on_key_press(key, Edit):
    if key in keybins.command:
        return keybins.command[key]()
    return key

def command_line_on_click(event, button, x, y, focus):
    app.mode.toggle_mode('command')

footer.message_line.on_enter = message_line_on_enter
footer.message_line.on_key_press = message_line_on_key_press
footer.message_line.on_click = message_line_on_click

footer.command_line.on_enter = command_line_on_enter
footer.command_line.on_key_press = command_line_on_key_press
footer.command_line.on_click = command_line_on_click
