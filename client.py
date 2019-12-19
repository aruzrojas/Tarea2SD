import xmlrpclib
import socket
from threading import Thread

#sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

class Servidor(Thread):
	def __init__(self,ip,port=0):
		Thread.__init__(self)
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.orig = (ip,port)

	def run(self):
		self.sock.bind(self.orig)
		while True:
			msj, cliente = self.sock.recvfrom(1024)
			print msj
		self.sock.close()



#sock.connect(("localhost",5000))


cliente = xmlrpclib.ServerProxy("http://localhost:5000")


ip = socket.gethostbyname(socket.gethostname())

server = Servidor(ip)
server.setDaemon(True)
server.start()
port = server.sock.getsockname()[1]
nombre_cliente = raw_input("ingresa tu nombre: ")

flag = True
while flag:
	if cliente.recibir_cliente(nombre_cliente, ip,port):
		flag = False
	else: 
		nombre_cliente = raw_input("ingresa otro nombre")
		continue


print ip,port



while True:
	listaclientes = cliente.lista_clientes()
	print("Lista de Clientes: ", listaclientes)
	destino = raw_input("Ingrese a quien desea mandarle un mensaje: ")
	for persona in listaclientes:

		if destino == persona[0]:

						

			msj=raw_input("Ingresa tu mensaje: ")

			canal = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			msj = "localhost:5000," + msj
			serv = ("localhost",5000)
			#canal.sendto(msj,serv)	 #msj = ip:port: MENSAJE (enviar al server)

			canal.close()

		else: 
			print("Opcion invalida, intentalo de nuevo")
	


print "Desconectandose del servidor"



