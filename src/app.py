import lib.urwid as urwid
import asyncio
import theme
from lib.ui.document import Document
from lib.mode import Mode

mode = Mode()

loop = urwid.MainLoop(
    Document,
    theme.palette,
    event_loop=urwid.AsyncioEventLoop(loop=asyncio.get_event_loop()),
    handle_mouse=False
)
loop.screen.set_terminal_properties(colors=256)
