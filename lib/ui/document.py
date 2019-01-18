import lib.urwid as urwid
import theme
from lib.ui.header import Header
from lib.ui.body import Body
from lib.ui.footer import Footer

Document = urwid.Frame(
    header=urwid.AttrMap(Header, theme.main_dark),
    body=urwid.AttrMap(Body, theme.main_dark),
    footer=urwid.AttrMap(Footer, theme.main_dark),
    focus_part='footer'
)
