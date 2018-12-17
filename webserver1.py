#最简单的Web Server
import socket

HOST,PORT="",8888

listen_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
"""listen_socket.bind(HOST,PORT) """
ip_post = ("127.0.0.1",8888)
listen_socket.bind(ip_post)
listen_socket.listen(1)

print("Serving HTTP on port %s ..." % PORT)

while True:
    client_connection,client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)

    http_response = """\
    http/1.1 200 OK 
    
    Hello World!
    """
    client_connection.sendall(bytes(http_response,encoding="utf-8"))

    client_connection.close()
