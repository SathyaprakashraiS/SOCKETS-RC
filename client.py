import socket
import time

HEADER=64
PORT=8998
FORMAT='utf-8'
DISCONNECT_MESSAGE="DISCONNECTED"
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
ACK="ACKNOWLEDGEMENT"



client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    if client.recv:
        #print("AWAKE")
        print("")
        print(client.recv(7878).decode(FORMAT))
        print("")
    else:
        #print("SLEEPING")
        print("NOTHING RECIEVED FROM SERVER")
        #time.sleep(3)

##send("Hello SATHYA")
##input()
#send("vankamm di mapla socket programm la erunthu")
##send("THIS IS A MESSAGE TO BE CAUGHT")
##input()
##send(":)")
##while c!=2:
##    c=int(input("TEST BUFFER 1.STAY2.EXIT"))
##    if(c==2):
##        send(DISCONNECT_MESSAGE)
##    else:
##        print("SLEEPING")
##        send("NOEN")
c=1
while(c!=3):
    print("")
    print("REQUESTING ACKNOWLEDGEMENT WITH NO USER REQUESTING MESSAGE LEADS TO ERROR")
    print("DO YOU WANT TO SEND MESSAGE OR QUIT")
    print("1.SEND MESSAGE")
    print("2.REQUEST ACKNOWLEDGEMENT")
    print("3.EXIT")
    c=int(input())
    if(c==1):
        #print("ENTER MESSAGE TO SEND")
        text=input("ENTER MESSAGE TO SEND :")
        send(text)
    if(c==2):
        send(ACK)
    if(c==3):
        send(DISCONNECT_MESSAGE)
    #else:
    #    send(DISCONNECT_MESSAGE)
    #    print("GIVE PROPER INPUTS")
