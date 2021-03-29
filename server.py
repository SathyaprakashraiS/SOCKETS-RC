import socket
import threading
import time

HEADER=64
PORT=8998
#SERVER="192.168.228.229"
SERVER=socket.gethostbyname(socket.gethostname())
FORMAT='utf-8'
DISCONNECT_MESSAGE="DISCONNECTED"
#(above code) this allows the code itself to find the ip address of the host system 
TOSEND="MR"
CONNECTED="CONNECTED"
REPLY="MSGTOALL"
MTS="MESSAGE TO ALL CLIENTS FROM SERVER"
ACK="ACKNOWLEDGEMENT"


s=[]
ACKFLAG=0
#code to make the socket stream data within it for clients
ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
 

def clientstream(conn,addr):
    print(f"NEW CONNECTION {addr} CONNECTED")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected=False
                print(f"ACTIVE USERS {threading.active_count()-2}")
                #print("LIST IS")
                #print(s)
            print(f"{addr} {msg}")
            #s.append(msg)
            ##29-03-2021#conn.send(f"MESSAGE RECIEVED : {msg}".encode(FORMAT))
            #conn.send(f"{msg}".encode(FORMAT))
            if msg == TOSEND:
                conn.send(f"{s}".encode(FORMAT))
                 
            if ((msg!=DISCONNECT_MESSAGE) or (msg!=TOSEND) or (msg!=CONNECTED) or (msg!=REPLY) or (msg!=ACK)):
                if((msg == TOSEND) or (msg == ACK) or (msg ==REPLY)):
                    print("TESTING APPEND FNCTION IF")
                    #conn.send(f"MESSAGE RECIEVED : {msg}".encode(FORMAT))
                    #print(s)
                    #s.append(msg)
                else:
                    #print("ELSE IFIFIF")
                    conn.send(f"MESSAGE RECIEVED : {msg}".encode(FORMAT))
                    print(s)
                    s.append(msg)

            if msg==REPLY:
                for c in clientlist:
                    c.sendall(f"{MTS}".encode(FORMAT))
            #conn.send("MESSAGE RECIEVED".encode(FORMAT))
            #conn.send(f"RECIEVED MESSAGE IS {msg}".encode(FORMAT)) inga poda thevailla becasue double print is WOT

            #if ((msg!=DISCONNECT_MESSAGE) or (msg!=TOSEND) or (msg!=CONNECTED)):
            #    print("TESTING APPEND FNCTION IF")
            #    s.append(msg)
    #conn.send(f"MESSAGE RECIEVED {msg}".encode(FORMAT))
    
    #with clients_lock:
        #for c in clients:
            #c.sendall(data)

    conn.close()
clientlist=set()
def start():
    server.listen()
    print(f"SERVER RUNNING ON {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=clientstream,args=(conn,addr))
        clientlist.add(conn)
        thread.start()
        print(f"ACTIVE CONNECTION {threading.active_count()-1}")
        #if(({threading.active_count()})==1 and (len(s)>0)):
        #    print("LIST IS ",s)

print("SERVER STARTED")
start()
