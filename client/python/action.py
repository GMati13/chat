from threading import Thread

def exit_from_app(app, client):
    if client.socket != None:
        client.disconnect()
    app.exit()

def run_socket_connection(client, url):
    Thread(target=lambda: client.connect(url)).start()
