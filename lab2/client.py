# https://github.com/aianta/cmput404-tcp-lab/blob/master/client.py

import socket

BYTES_TO_READ = 4069

def get(host, port):
    request = b"GET / HTTP/1.1\nHost:" + host.encode("utf-8") + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect((host, port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)
    
    result = s.recv(BYTES_TO_READ)
    while len(result) > 0:
        # read until no more data
        print(result)
        result = s.recv(BYTES_TO_READ)
    
    s.close()
    
    
get("www.google.com", 80)  # port 80 is the standard port for HTTP requests that aren't encrypted