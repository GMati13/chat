#!/usr/bin/env python3

from client import client
import handlers as handler
import ui

client.start()

ui.msg_line.on_enter = handler.msg_line_on_enter
ui.msg_line.on_key_press = handler.msg_line_on_key_press

ui.cmd_line.on_enter = handler.cmd_line_on_enter
ui.cmd_line.on_key_press = handler.cmd_line_on_key_press

ui.window.run()
