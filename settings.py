class Settings:

	def __init__(self):
		self.screen_width = 800
		self.screen_height = 400

		self.gravity = 1
		self.bg_color = (60, 60, 60)
		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.points = 2
		self.obstacle_speed = 10

	def increase_speed(self):
		self.points *= self.speedup_scale
		self.obstacle_speed *= self.speedup_scale
