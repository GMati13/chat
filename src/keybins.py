import lib.ui.body as body
import src.app as app
import src.handlers.client.chats as chats

normal = {
    ':': lambda: app.mode.toggle_mode('command'),
    'i': lambda: app.mode.toggle_mode('message')
}

command = {
    'esc': lambda: app.mode.toggle_mode(app.mode.previous_mode)
}

message = {
    'esc': lambda: app.mode.toggle_mode(app.mode.previous_mode)
}

dialogs = {
    ':': lambda: app.mode.toggle_mode('command'),
    'j': lambda: body.history.scroll_next(),
    'k': lambda: body.history.scroll_prev(),
    'J': lambda: 'down',
    'K': lambda: 'up'
}

chat = {
    ':': lambda: app.mode.toggle_mode('command'),
    'j': lambda: body.history.scroll_next(),
    'k': lambda: body.history.scroll_prev(),
    'J': lambda: 'down',
    'K': lambda: 'up',
    'i': lambda: app.mode.toggle_mode('message'),
    'esc': lambda: app.mode.toggle_mode('normal')
}
