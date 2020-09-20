import sys                                         #we'll use sys module to exit the game when player quite.
import pygame
from setting_alien_invasion import Setting 
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button


def run_game():
	
	#initialize game and creating sacreen object
	pygame.init()
	ai_setting = Setting()
	sacreen = pygame.display.set_mode((ai_setting.sacreen_width,ai_setting.sacreen_height))              #(1200,800) that define the dimension of window sacreen 
	pygame.display.set_caption("Alien Invasion")   
	
	# Make a ship, a group of bullets, and a group of aliens.
	ship = Ship(ai_setting,sacreen) 
	bullets = Group()
	aliens = Group()      
	#create the fleet_aliens
	gf.create_fleet(ai_setting,sacreen,ship,aliens) 
	
	# Create an instance to store game statistics.
	stats = GameStats(ai_setting)                                            
	alien = Alien(ai_setting,sacreen)
	
	
	play_button = Button(ai_setting,sacreen,'Play')
	#start the main loop for the game
	while True:
		#watch keyboard and mouse event
		gf.check_events(ai_setting,sacreen,ship,bullets)
		
		if stats.game_active:
			ship.update()
			
			gf.update_bullets(ai_setting,sacreen,ship,aliens,bullets)
			gf.update_aliens(ai_setting,stats,ship,sacreen,aliens,bullets)	
		gf.update_sacreen(ai_setting, sacreen, ship, aliens, bullets)
		
		for event in pygame.event.get():					                            
			if event.type == pygame.QUIT:   				                            
				sys.exit()
		# Make the most recently drawn screen visible.
		sacreen.fill(ai_setting.bg_color) 
		ship.blitme()								       	                           
		pygame.display.flip()                                                         
run_game()                                                                             

