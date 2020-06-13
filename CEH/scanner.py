#!/bin/python3
import sys #allows us to enter command line arguements
import socket
from datetime import datetime as dt
#define our target
if len(sys.argv)==2:
    target= socket.gethostbyname(sys.argv[1]) #translate a hostname to ipv4
else:
    print("Invalid amount of arguements. ")
    print("Syntax : python3 scanner.py <ip>")
    sys.exit()
#Add a pretty banner
print("-"*50)
print("Scanning target "+target)
print("Time started :"+str(dt.now()))
print("-"*50)
#AF_INET is ipv4, SOCK_STREAM is port
try:
    for port in range(18,85):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #this is a float
        result=s.connect_ex((target,port)) #returns error indicator on connection
        print("Checking port {} ".format(port))
        if result==0:
            print("Port: {} is open".format(port))
            s.close()
except KeyboardInterrupt:
    print("\nExiting program .")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit