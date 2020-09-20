import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self,ai_setting,sacreen):
		super(Alien,self).__init__()
		self.ai_setting = ai_setting
		self.sacreen = sacreen
	
		self.image = pygame.image.load("images/alien.png")
		self.rect = self.image.get_rect()
		#start form alien from top-left corner
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#store the alien exact position
		self.x = float(self.rect.x)
		
	def blitme(self):
		#draw the alien at its current position
		self.sacreen.blit(self.image,self.rect)

	def update(self):
		self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
		self.rect.x = self.x
	
	def check_edges(self):
		sacreen_rect = self.sacreen.get_rect()
		if self.rect.right >= self.rect.right:
			return True
		elif self.rect.left <= 0:
			return True
			
