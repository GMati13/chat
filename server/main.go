package main

import (
  "fmt"
  "net/http"
  "github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader {
  ReadBufferSize:  1024,
  WriteBufferSize: 1024,
}

var connections = make(map[string]*websocket.Conn)

func main() {
  http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    conn, _ := upgrader.Upgrade(w, r, nil) // error ignored for sake of simplicity

    addr := conn.RemoteAddr()

    connections[addr.String()] = conn

    for {
      // Read message from browser
      msgType, msg, err := conn.ReadMessage()
      if err != nil {
        return
      }

      // Print the message to the console
      fmt.Printf("%s sent: %s\n", addr, string(msg))

      // Write message back to browser
      for a, c := range connections {
        if a != addr.String() {
          c.WriteMessage(msgType, []byte("< " + string(msg)))
        }
      }
    }
  })

  fmt.Println("Server is listening...")
  http.ListenAndServe("0.0.0.0:8181", nil)
}
