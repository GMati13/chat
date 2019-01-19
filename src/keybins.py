import lib.ui.body as body
import src.app as app

normal = {
    ':': lambda: app.mode.toggle_mode('command'),
    'i': lambda: app.mode.toggle_mode('message')
}

command = {
    'esc': lambda: app.mode.toggle_mode(app.mode.previous_mode)
}

message = {
    'esc': lambda: app.mode.toggle_mode('normal')
}

dialogs = {
    ':': lambda: app.mode.toggle_mode('command'),
    'j': lambda: body.history.scroll_next(),
    'k': lambda: body.history.scroll_prev(),
    'J': lambda: body.history.scroll_page_down(),
    'K': lambda: body.history.scroll_page_up(),
    'esc': lambda: app.mode.toggle_mode('normal')
}
