import socket
recv_ip='127.0.0.1'
recv_port=4444
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))
while True:
	data=s.recvfrom(1000)
	if len(data) >150:
		print("Message length exceeded")
	else:
		ndata=data[0].decode('ascii')
		print("Data from sender: ",ndata)
s.close()
