import threading
import sys
import socket
import pickle
import os
import platform






class Cliente():

	def __init__(self, host=socket.gethostname(), port=59989):
		self.sock = socket.socket()
		self.sock.connect((str(host), int(port)))
		hilo_recv_mensaje = threading.Thread(target=self.recibir)
		hilo_recv_mensaje.daemon = True
		hilo_recv_mensaje.start()
		host = socket.gethostname()
		ip = socket.gethostbyname(host)
		print('Hilo con PID',os.getpid())
		print('Hilos activos', threading.active_count())
		print('Procesador', platform.processor())
		print('Release', platform.release())
		print('Sistema', platform.system())
		print('Version', platform.version())
		print('Cores Fisicos', os.cpu_count()/2)
		print('IPV4', ip)
              
              
		while True:
			msg = input('\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n')
			if msg != 'Q' :
				self.enviar(msg)
			else:
				print(" **** TALOGOOO  ****")
				self.sock.close()
				sys.exit()

	def recibir(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def enviar(self, msg):
		self.sock.send(pickle.dumps(msg))

c = Cliente()

		