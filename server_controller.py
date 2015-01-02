from camera_feed import Camera_Server_Handler, ThreadedHTTPServer
import threading
import time

class Server_Controller:
	def __init__(self):
		self.server = ThreadedHTTPServer(('', 8080), Camera_Server_Handler)

	def start(self):
		"""self.keep_running = True
		while self.keep_running:
			self.server.handle_request()"""
		self.server.serve_forever()

		print 'controller stopped, returning...'

		return

	def stop(self):
		self.server.shutdown()
		#self.keep_running = False
		
		#self.server.socket.close()

"""if __name__ == '__main__':

	controller = Server_Controller()
	print 'starting'
	t = threading.Thread(target = controller.start)
	t.start()
	print 'sleeping'
	time.sleep(2)
	print 'stopping'
	controller.stop()
	print 'joined'
	exit()"""
