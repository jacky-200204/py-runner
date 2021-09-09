import pygame

class Player:
	"""Overall class to manage the player"""

	def __init__(self, px_runner):
		self.screen = px_runner.screen
		self.bg = px_runner.bg
		self.settings = px_runner.settings

		self.player_img = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
		self.player_rect = self.player_img.get_rect(centerx=80)
		self.player_rect.bottom = self.bg.ground_rect.top

	def draw(self):
		"""Draws the player."""
		self.screen.blit(self.player_img, self.player_rect)

	def jump(self):
		"""Make the player jump."""
		self.settings.gravity = -20

	def update(self):
		"""Updates the player."""
		self.player_rect.y += self.settings.gravity
		self.settings.gravity += 2
		if self.player_rect.bottom >= self.bg.ground_rect.top:
			self.player_rect.bottom = self.bg.ground_rect.top

	def check_bottom(self):
		if self.player_rect.bottom >= self.bg.ground_rect.top:
			return True
		return False