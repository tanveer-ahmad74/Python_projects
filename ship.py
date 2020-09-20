import pygame

class Ship():
	
	def __init__(self,ai_setting,sacreen):
		"""Initialize the ship and starting position"""
		self.sacreen = sacreen
		self.ai_setting = ai_setting 
		'''Load the ship image and gets its rect'''
		self.image = pygame.image.load("images/ships.png")
		self.rect = self.image.get_rect()                       #rect means rectangle
		self.sacreen_rect = sacreen.get_rect()                  #set the sacreen according to the x-coordinate
		
		#start each new ship at the bottom center of the sacreen
		self.rect.centerx = self.sacreen_rect.centerx   
		self.rect.bottom = self.sacreen_rect.bottom
		self.center = float(self.rect.centerx)
		
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		if self.moving_right and self.rect.right < self.sacreen_rect.right:
			self.center += self.ai_setting.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_setting.ship_speed_factor
		
	def blitme(self):
		"""Draw ship at its current location"""
		self.sacreen.blit(self.image,self.rect)
		
	def center_ship(self):
		self.center = self.sacreen_rect.centerx
