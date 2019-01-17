from threading import Thread
import json

def exit_from_app(app, client):
    if client.socket != None:
        client.disconnect()
    app.exit()

def run_socket_connection(client, url=None):
    Thread(target=lambda: client.connect(url)).start()

def send_message(client, text, author):
    if client.socket != None and text.strip():
        client.socket.send(json.dumps({
            'author': author,
            'text': text
            }))
