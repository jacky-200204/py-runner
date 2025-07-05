import pygame

class Player:
	"""Overall class to manage the player"""

	def __init__(self, px_runner):
		self.screen = px_runner.screen
		self.bg = px_runner.bg
		self.settings = px_runner.settings
		
		player_img1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
		player_img2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
		self.jump_img = pygame.image.load("graphics/player/jump.png").convert_alpha()
		self.player_img_list = [player_img1, player_img2]
		self.index = 0

		self.initialize_img()
		self.rect = self.image.get_rect(centerx=80)
		self.rect.bottom = self.bg.ground_rect.top

	def draw(self):
		"""Draws the player."""
		self.screen.blit(self.image, self.rect)

	def jump(self):
		"""Make the player jump."""
		self.settings.gravity = -22

	def down_player(self):
		self.rect.bottom = self.bg.ground_rect.top

	def update(self):
		"""Updates the player."""
		self.rect.y += self.settings.gravity
		self.settings.gravity += 2
		if self.rect.bottom >= self.bg.ground_rect.top:
			self.rect.bottom = self.bg.ground_rect.top
		self.animate_player()

	def initialize_img(self):
		self.image = self.player_img_list[int(self.index)]

	def animate_player(self):
		self.index += 0.3
		if self.index >= len(self.player_img_list):
			self.index = 0
		if self.rect.bottom <= self.bg.ground_rect.top:
			self.initialize_img()

	def check_bottom(self):
		if self.rect.bottom >= self.bg.ground_rect.top:
			return True
		return False