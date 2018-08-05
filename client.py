from socket import *
import sys
import ipaddress

def retornaIpv6(server_name):
	resposta = gethostbyaddr(server_name)
	resposta2 = str(resposta[2])
	resposta2 = resposta2.strip('[')
	resposta2 = resposta2.strip(']')
	resposta2 = resposta2.strip("'")
	try:
		ipaddress.IPv6Address(resposta2)
		return resposta2
	except Exception as e:
		return '::ffff:'+resposta2

if __name__ == "__main__":
	server_name = retornaIpv6(sys.argv[1])
	server_port = int(sys.argv[2])
	client_socket = socket(AF_INET6, SOCK_STREAM)
	client_socket.connect((server_name, server_port))
	while True:
		msg = input()
		if msg == 'X': break
		client_socket.send(msg.encode())
		rcv_msg = client_socket.recv(2048)
		rcv_msg = rcv_msg.decode()
		print (rcv_msg)
	client_socket.close()
