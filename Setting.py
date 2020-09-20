class Setting():
	
	def __init__(self):
		self.sacreen_width = 1200
		self.sacreen_height = 800
		self.bg_color = (230,230,230)
		
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		
		self.bullet_speed_factor = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 3
		
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
	
	# ~ def initialize_dynamic_setting(self):
		# ~ self.ship_speed_factor = 1.5
		# ~ self.bullet_speed_factor = 3
		# ~ self.alien_speed_factor = 1
		# ~ self.fleet_direction = 1
		
	# ~ def increase_speed(self):
		# ~ self.ship_speed_factor *= self.speedup_scale
		# ~ self.bullet_speed_factor *= self.speedup_scale
		# ~ self.alien_speed_factor *= self.speedup_scale
