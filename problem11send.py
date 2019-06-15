import socket
recv_ip='127.0.0.1'
recv_port=4444
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	msg=input("Enter message: ")
	s.sendto(msg.encode('ascii'),(recv_ip,recv_port))
	if msg=='q':
		exit()
s.close()


