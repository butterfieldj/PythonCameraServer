import pygame
import time

# Class used in playing sound when motion is detected
class Alarm_Controller:
	alarm = 'sounds/alarm.wav' # Static addresses of sound files

	# Constructor, initializes pygame sound player
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.sound = pygame.mixer.Sound(self.alarm)


	# Plays sound and waits for sound to finish before continuing
	def play_sound(self):
		self.sound.play()
		time.sleep(3)
