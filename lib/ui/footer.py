import lib.urwid as urwid
import theme

message_line = urwid.EditText()
status_line = urwid.StatusLine()
command_line = urwid.EditText()
info_line = urwid.StatusLine()

tools = urwid.ListBox([
    urwid.AttrMap(message_line, theme.main_dark, theme.main_light),
    urwid.AttrMap(status_line, theme.main_dark),
    urwid.AttrMap(command_line, theme.main_dark, theme.main_light)
])

Footer = urwid.BoxAdapter(urwid.ListBox([
    urwid.AttrMap(info_line, theme.main_dark),
    urwid.BoxAdapter(tools, 3)
]), 4)
