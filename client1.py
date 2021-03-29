import socket
import time

HEADER=64
PORT=8998
FORMAT='utf-8'
DISCONNECT_MESSAGE="DISCONNECTED"
SERVER=socket.gethostbyname(socket.gethostname())
#SERVER="192.168.56.10"
#ADDR=("192.168.56.10",8998)
ADDR=(SERVER,PORT)
TOSEND="MR"
towork=[]
check=""
REPLY="MSGTOALL"


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    if(msg==TOSEND):
        message=msg.encode(FORMAT)
        msg_length=len(message)
        send_length=str(msg_length).encode(FORMAT)
        send_length+=b' ' * (HEADER-len(send_length))
        client.send(send_length)
        client.send(message)
        #check=client.recv(7878).decode(FORMAT)
        #towork.append(check)
        #print(check)
        if client.recv:
            print("INSIDE TOSEND SEND RECV FUNCTION")
            print("")
            #towork.append(client.recv(7878).decode(FORMAT))
            #check=client.recv(7878).decode(FORMAT)
            #print("")
            ###check=client.recv(7878).decode(FORMAT)
            towork.append(client.recv(7878).decode(FORMAT))
            print("")
            #print(check)
            #recently removered#print("THE CHECK RECIEVED")
            #recently removed#print(check)
            #print(client.recv(7878).decode(FORMAT))
            #towork.append(check)
            print("SENDING ACKNOWLEDGEMENT")
            print("")
            send(REPLY)
            print(towork)
            towork.clear()
            #print(check)
        else:
            print("SLEEPING")
            print("")
            #time.sleep(3)
    else:
        message=msg.encode(FORMAT)
        msg_length=len(message)
        send_length=str(msg_length).encode(FORMAT)
        send_length+=b' ' * (HEADER-len(send_length))
        client.send(send_length)
        client.send(message)
        if client.recv:
            #print("AWAKE")
            #towork.append(client.recv(7878).decode(FORMAT))
            #check=client.recv(7878).decode(FORMAT)
            print(client.recv(7878).decode(FORMAT))
            print("")
            
            #print(check)
        else:
            print("SLEEPING")
            #time.sleep(3)


##c=0
##send("CONNECTED")
##input()
##send(REPLY)
##send(TOSEND)
##while c!=2:
##    c=int(input("TEST BUFFER 1.STAY2.EXIT"))
##    if(c==2):
##        send(DISCONNECT_MESSAGE)
##    else:
##        print("SLEEPING")
        #print(towork[0])
    #dodo=towork[0]
    #dod0=dodo[28:107]
    #print(dodo)
    #for i in towork:
    #    if(towork[i]=="CONECTED" or towork=="TO SEND"):
    #        towork[i]=" "
c=1
while(c!=3):
    print("")
    print("REQUESTING ACKNOWLEDGEMENT WITH NO USER REQUESTING MESSAGE LEADS TO ERROR")
    print("DO YOU WANT TO SEND MESSAGE OR QUIT")
    print("1.SEND MESSAGE")
    print("2.REQUEST MESSAGE")
    print("3.EXIT")
    c=int(input())
    if(c==1):
        text=input("ENTER MESSAGE TO SEND :")
        send(text)
    if(c==2):
        send(TOSEND)
    if(c==3):
        send(DISCONNECT_MESSAGE)
    #else:
    #    send(DISCONNECT_MESSAGE)
    #    print("GIVE PROPER INPUTS")
