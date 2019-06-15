import socket
recv_ip='127.0.0.1'
recv_port=4444
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=input()
while True:
	if ip=='1':
		msg=input("Enter message: ")
		s.sendto(msg.encode('ascii'),(recv_ip,recv_port))
		data=s.recvfrom(100)
		ndata=data[0].decode('ascii')
		print("Message: ",ndata)
	if ip=='2':
		msg=input("Enter message: ")
		s.sendto(msg.encode('ascii'),(recv_ip,recv_port))


