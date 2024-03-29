import sys
import websocket

class MyWebSocketApp(websocket.WebSocketApp):
    def send(self, data, on_error=None):
        try:
            super(MyWebSocketApp, self).send(data)
        except websocket._exceptions.WebSocketConnectionClosedException:
            if on_error != None:
                on_error('Connection already closed')

class WSClient:
    def __init__(self, url=None, on_open=None, on_message=None, on_close=None, on_error=None):
        self.on_open = on_open
        self.on_message = on_message
        self.on_close = on_close
        self.on_error = on_error
        self.socket = None
        self.url = url
            
    def connect(self, url=None):
        url = self.url if url == None else url
        socket = MyWebSocketApp(url,
                                on_message = self.on_message,
                                on_error = self.on_error,
                                on_close = self.on_close)
        socket.on_open = self.on_open
        self.socket = socket
        socket.run_forever()

    def disconnect(self):
        self.socket.close()
        self.socket = None

url = sys.argv[1] if len(sys.argv) > 1 else 'ws://localhost:8181'

client = WSClient(url)
