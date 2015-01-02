import numpy
import cv2
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import threading
import time
from os import curdir, sep

class Camera_Server_Handler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.capture = cv2.VideoCapture(0)
		print self.path
		try:
			if self.path.endswith("index.html"):
				f = open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
				return
			if self.path.endswith(".mjpeg"):
				self.send_response(200)
				self.wfile.write("Content-Type: multipart/x-mixed-replace; boundary=--aaboundary")
				self.wfile.write("\r\n\r\n")
				
				while 1:
					val, image = self.capture.read()
					_,data = cv2.imencode('.jpeg', image, [1,90])
					jpegString = data.tostring()
					self.wfile.write("--aaboundary\r\n")
					self.wfile.write("Content-Type: image/jpeg\r\n")
					self.wfile.write("Content-length: " + str(len(jpegString)) + "\r\n\r\n")
					self.wfile.write(jpegString)
					self.wfile.write("\r\n\r\n\r\n")
					#self.capture.release()
					time.sleep(0.1)
				
		except IOError:
			self.send_error(404, 'Not found')

		self.capture.release()

		return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handles requests in a separate thread"""
