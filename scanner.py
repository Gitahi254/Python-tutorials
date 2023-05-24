import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate host name to Ipv4
else:
    print('Invalid amounts of arguments')
    print('Syntax: python3 scanner.py <ip>')

#Add a pretty banner
print('-' * 50)
print('Scanning target: +target')
print('Time started:' +str(datetime.now()))
print('-' * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f'port{port}is open')
        s.close()

except KeyboardInterrupt:
    print('\nExisting program.')
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved')
    sys.exit()

except socket.error:
    print('Could not connect to server.')
    sys.exit()