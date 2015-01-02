import socket
import threading
from server_controller import Server_Controller
from alarm_controller import Alarm_Controller

class Socket_Listener:
	def __init__(self):
		self.server_controller = Server_Controller()
		self.alarm_controller = Alarm_Controller()
		self.server_running = False

	def start_command(self, command):
		if(command == "start"):
			print 'starting server...'
			t = threading.Thread(target = self.server_controller.start)
			t.start()
			self.server_running = True
			print 'started server'
		elif(command == "stop"):
			print 'stopping server...'
			self.server_controller.stop()
			self.server_running = False
			print 'server stopped'
		elif(command == "alarm"):
			print 'playing sound'
			if self.server_running:
				self.alarm_controller.play_sound()
		return

	def start_listening(self):
		HOST = ''
		PORT = 12345

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print 'created'

		try:
			s.bind((HOST, PORT))
			print 'bound'
		except:
			print 'error'
			exit()

		s.listen(5)
		print 'listening...'

		try:
			while 1:
				conn, addr = s.accept()
				print 'Connected with ' + addr[0] + ' : ' + str(addr[1])
				data = conn.recv(1024)
				if not data:
					break
				else:
					print str(data)
					self.start_command(str(data).strip())
				conn.close()
		except KeyboardInterrupt:
			s.close()
