import socket
recv_ip='127.0.0.1'
recv_port=4444
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))
ip=input()
while True:
	if ip=='2':
		data=s.recvfrom(100)
		ndata=data[0].decode('ascii')
		print("Data from sender: ",ndata)
	if ip=='1':
		data=s.recvfrom(100)
		ndata=data[0].decode('ascii')
		print("Data from sender: ",ndata)
		rply=input("Type your reply:")
		s.sendto(rply.encode('ascii'),data[1])
s.close()
