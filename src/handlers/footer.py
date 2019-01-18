import lib.ui.body as body
import lib.urwid as urwid
import lib.ui.footer as footer
import src.app as app

def message_line_on_enter(value, Edit):
    body.history.append_child(urwid.Text(value))
    body.history.scroll_down()
    Edit.clear()

def message_line_on_click(event, button, x, y, focus):
    app.mode.toggle_mode('normal')
    body.history.clear()

def command_line_on_click(event, button, x, y, focus):
    app.mode.toggle_mode('command')

footer.message_line.on_enter = message_line_on_enter
footer.message_line.on_click = message_line_on_click

footer.command_line.on_click = command_line_on_click
