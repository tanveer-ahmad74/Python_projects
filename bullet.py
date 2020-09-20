import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	
	def __init__(self,ai_setting,sacreen,ship):
		super(Bullet,self).__init__()
		self.sacreen = sacreen
		self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = (self.rect.y)
		self.color = ai_setting.bullet_color
		self.speed_factor = ai_setting.bullet_speed_factor
	
	def update(self):
		self.y -= self.speed_factor
		self.rect.y = self.y
		
	def draw_bullet(self):
		pygame.draw.rect(self.sacreen,self.color,self.rect)
		
