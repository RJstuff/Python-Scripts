import socket

import sys

def create_socket():
    try:
        global host
        global port
        global s

        host = " "
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("socket creation error :"+str(msg))

def bind_socket():
    try:
        global host
        global port
        global s

        print("binding the port" + str(port))

        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("binding error "+str(msg)+"\n" + ".....retrying")

        bind_socket()

def socket_accept():
    conn,address = s.accept()
    print("connection has been established" + " IP : " + address[0] + "Port :" + str(address[1]))
    send_command(conn)
    conn.close()

def send_command(conn):
    while True:
        cmd = input()
        if cmd == "exit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            cnn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"qtf-a")
            print(client_response, end ="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
    
