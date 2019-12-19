import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import socket

listaclientes = []

#class cliente:

#	def __init__(self,nombre,ip):
#		self.nombre = nombre
#		self.ip = ip

def enviar_mensaje(nombreorigen,ipdest,portdest):

	





def thread_recibe(ip):

	mensaje = conexion.recv(1024)
	destino, mensaje = mensaje.split(",")
	destino = destino.split(":")
	conexion.sendto(mensaje,destino)
	conexion.close()




def recibir_cliente(nombre,ip,port):


	if listaclientes == []:

		listaclientes.append((nombre,ip,port))
		print listaclientes
		ip = listaclientes[0][1]
		port = listaclientes[0][2]
		print ip,port
		mensaje = "Hola Cliente "
		canal = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		de = (ip,int(port))
		canal.sendto(mensaje,de)
		canal.close()

		return 1
		
	for cliente in listaclientes:
		print(cliente)
		if nombre in cliente:
			print "Este nombre ya esta ocupado"
			return 0
		else: 
			listaclientes.append((nombre,ip,port))
			print(listaclientes)
			return 1
	print("salgo")
	return 0

def lista_clientes():
	return listaclientes

def eliminar_cliente(nombre):

	return



ip = "localhost"
puerto = 5000
server = SimpleXMLRPCServer((ip,puerto))

print "servidor corriendo en" ,ip,":",puerto

server.register_function(recibir_cliente)
server.register_function(lista_clientes)
server.register_function(eliminar_cliente)
server.serve_forever()


