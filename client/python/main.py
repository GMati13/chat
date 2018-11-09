#!/usr/bin/env python3

import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

server = input('server: ')

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        cmd = ''
        while cmd != 'exit':
            if cmd != '':
                ws.send(cmd)
            cmd = input()
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    ws = websocket.WebSocketApp('ws://{}'.format(server),
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
