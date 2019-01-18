import lib.ui.footer as footer
import src.app as app
import src.templates.statusline as status_line

def on_init(mode):
    footer.status_line.left_column.set_text(status_line.app_status_left.format(
        mode=mode,
        username='Tester',
        online='offline'
    ))

def on_toggle(prev_mode, next_mode):
    footer.status_line.left_column.set_text(status_line.app_status_left.format(
        mode=next_mode,
        username='Tester',
        online='offline'
    ))

app.mode.on_init = on_init
app.mode.on_toggle = on_toggle

app.mode.init()
