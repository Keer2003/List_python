import socket
import os
try:
    hostName=socket.gethostname()
    print(hostName)
    ipaddress=socket.gethostbyname(hostName)
    print(ipaddress)
    pingcmd='{0} --{1} "{2}"',format('ping','t',ipadress)
    print(pingcmd)
except Exception as e:
    print(e)
