import pygame.font

class ScoreBoard():
	
	def __init__(self):
		self.sacreen = sacreen
		self.sacreen_rect = sacreen.get_rect()
		self.ai_setting = ai_setting
		self.stats = stats
		
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)
		self.prep_score()
		
	def prep_score(self):
		
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def show_score(self):
		self.sacreen.blit(self.score_image, self.score_rect)
