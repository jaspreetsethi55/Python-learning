import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
 
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# connect() for UDP doesn't send packets
s.connect(('10.0.0.0', 0))
print(s.getsockname()[0])
