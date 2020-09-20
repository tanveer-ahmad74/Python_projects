import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_setting,sacreen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True	
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True		
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_setting,sacreen,ship,bullets)		
	elif event.key == pygame.K_q:
		sys.exit()
	
def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False	
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	
def check_events(ai_setting,sacreen,ship,bullets):
	"""Respond to keypressess and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_setting,sacreen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
		
def update_sacreen(ai_setting,sacreen,ship,alien,bullets):
	sacreen.fill(ai_setting.bg_color)
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	alien.draw(sacreen)
	sb.show_score()
	pygame.display.flip()	

def fire_bullet(ai_setting,sacreen,ship,bullets):
	if len(bullets) < ai_setting.bullets_allowed:
			new_bullet = Bullet(ai_setting,sacreen,ship)
			bullets.add(new_bullet)

def update_bullets(ai_setting,sacreen,ship,aliens,bullets):
	bullets.update()
	
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)		
	check_bullet_alien_collisions(ai_setting,sacreen,ship,aliens,bullets)
	
def check_bullet_alien_collisions(ai_setting, sacreen, ship, aliens, bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
		ai_setting.increase_speed()
		create_fleet(ai_setting,sacreen,ship,aliens)
		
def get_number_aliens_x(ai_setting,alien_width):
	available_space_x = ai_setting.sacreen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_setting, ship_height, alien_height):
	available_space_y = (ai_setting.sacreen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
	
def create_alien(ai_setting,sacreen,aliens,alien_number,row_number):
	alien = Alien(ai_setting,sacreen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
	
		
def create_fleet(ai_setting,sacreen,ship,aliens):
	alien = Alien(ai_setting,sacreen)
	number_aliens_x = get_number_aliens_x(ai_setting,alien.rect.width)
	number_rows = get_number_rows(ai_setting,ship.rect.height,alien.rect.height)
	
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_setting,sacreen,aliens,alien_number,row_number)
		
def check_fleet_edges(ai_setting,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_setting,aliens)
			break
				
def change_fleet_direction(ai_setting,aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_setting.fleet_drop_speed	
	ai_setting.fleet_direction *= -1
	
def ship_hit(ai_setting,stats,sacreen,ship,aliens,bullets):
	if stats.ship_left > 0:
		stats.ship_left = -1
		aliens.empty()
		bullets.empty()
		create_fleet(ai_setting,sacreen,ship,aliens)
		ship.center_ship()
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_setting,stats,sacreen,ship,aliens,bullets):
	sacreen_rect = sacreen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= sacreen_rect.bottom:
			ship_hit(ai_setting,stats,sacreen,ship,aliens,bullets)
			break
				
def update_aliens(ai_setting,stats,sacreen,ship,aliens,bullets):
	check_fleet_edges(ai_setting,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_setting,stats,sacreen,ship,aliens,bullets)
	check_aliens_bottom(ai_setting,stats,sacreen,ship,aliens,bullets)


	
