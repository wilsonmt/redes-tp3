from socket import *
import _thread
import sys
from GerenciadorDeMensagens import *

def con_client(conn_socket, client_addr,):
	print (cliente_addr, "conectado!")
	while True:
		msg = conn_socket.recv(2048)
		if not msg: break
		print (cliente_addr, msg.decode())
		gerenciador = GerenciadorDeMensagens.getInstance()
		new_msg = gerenciador.interpreta(msg.decode())
		new_msg = new_msg.encode()
		conn_socket.send(new_msg)
	print (cliente_addr, "desconectado...")
	conn_socket.close()

if __name__ == "__main__":
	server_port = int(sys.argv[1])
	server_socket = socket(AF_INET6, SOCK_STREAM)
	server_socket.bind(("", server_port))
	server_socket.listen(100)
	while True:
		conn_socket, cliente_addr = server_socket.accept()
		_thread.start_new_thread(con_client,(conn_socket,cliente_addr))
	conn_socket.close()
