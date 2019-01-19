#!/usr/bin/env python3
from client import client
import src.app as app
import src.handlers.footer
import src.handlers.body
import src.handlers.mode
import src.storage as store
import src.handlers.client.listeners

client.start()

app.mode.init()
app.loop.run()
