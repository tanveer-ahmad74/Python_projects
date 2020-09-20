import pygame.font

class Button():

	def __init__(self,ai_setting,sacreen,msg):
		self.sacreen = sacreen
		self.sacreen_rect = sacreen.get_rect()
		
		self.width , self.height = 150,60
		self.button_color = (180,180,180)
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None,48)
		
		self.rect = pygame.Rect(0, 0, self.width,self.height)
		self.rect.center = self.sacreen_rect.center
		
		self.prep_msg(msg)
	
	def prep_msg(self,msg):
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		self.sacreen.fill(self.button_color,self.rect)
		self.sacreen.blit(self.msg_image,self.msg_image_rect)
		
