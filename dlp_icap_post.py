import socket
import os
# construct http body
httpBody = "2d\r\n" 
httpBody += "I am posting aba 11nformation.  ICAP powered!\r\n"
httpBody += "0\r\n"
httpBody += "\r\n"

# construct http header
httpHeader = "POST /origin-resource/form.pl HTTP/1.1\r\n"
httpHeader += "Host: www.origin-server.com\r\n"
httpHeader += "Accept: text/html, text/plain\r\n"
httpHeader += "Accept-Encoding: compress\r\n"
httpHeader += "Pragma: no-cache\r\n"
httpHeader += "\r\n"

# construct icap request 
request = "REQMOD icap://10.87.1.94/reqmod ICAP/1.0\r\n"
request += "Host: 10.87.1.94\r\n"
request += "X-Client-Abandon-Supported: 1\r\n"
request += "X-Scan-Progress-Interval: 10\r\n"
#request += "X-Authenticated-User: ZHA=\r\n"
request += "X-Client-IP: 10.150.128.158\r\n"
request += "X-Server-IP: 144.208.69.31\r\n"
#request += "X-Authenticated-User: V2luTlQ6Ly9TWU1DRExQTEFCL2Rw\r\n"
#request += "X-Bluecoat-Transaction-UUID: df3cedfc6c0e4171-000000000001c8fd-000000005c4d1199\r\n"
request += "Encapsulated: req-hdr=0, req-body=%i\r\n" % (len(httpHeader))
request += "\r\n"
request += httpHeader
#request += "\r\n"
request += httpBody
#request += "\r\n"

# establish TCP connection with icap server
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(('127.0.0.1', 1344))
print(request)

# send icap request
for i in range(0,500):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.87.1.94', 1344))
    print("Sending Request number:" + str(i))
    s.send(request.encode())
    s.close()
# receive response from icap server
data = s.recv(1024)#
print(data)

