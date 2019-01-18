import lib.urwid as urwid
import theme

contacts = urwid.List()
history = urwid.List()

Body = urwid.Columns([
    urwid.AttrMap(history, theme.main_light)
], dividechars=1, min_width=1)
