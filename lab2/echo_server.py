# https://github.com/aianta/cmput404-tcp-lab/blob/master/echo_server.py

import socket

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
    with conn:  # conn is a socket (directly connected to the client)
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:  # if the socket collapses/socket shut downs
                break
            print(data)
            conn.sendall(data)  # send data back (echo server)

def start_server():
    # create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # bind to host and port
        s.bind((HOST, PORT))
        # set socket options
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # listen on host and port
        s.listen()
        
        # accept an incoming connection to host and port and returns the connection that was made
        # as well as the address where it came from
        conn, addr = s.accept()
        handle_connection(conn, addr)
        
start_server()