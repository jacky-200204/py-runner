import pygame

class Player:
	"""Overall class to manage the player"""

	def __init__(self, px_runner):
		self.screen = px_runner.screen
		self.bg = px_runner.bg
		self.settings = px_runner.settings

		self.player_img = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
		self.rect = self.player_img.get_rect(centerx=80)
		self.rect.bottom = self.bg.ground_rect.top

	def draw(self):
		"""Draws the player."""
		self.screen.blit(self.player_img, self.rect)

	def jump(self):
		"""Make the player jump."""
		self.settings.gravity = -22

	def update(self):
		"""Updates the player."""
		self.rect.y += self.settings.gravity
		self.settings.gravity += 2
		if self.rect.bottom >= self.bg.ground_rect.top:
			self.rect.bottom = self.bg.ground_rect.top

	def check_bottom(self):
		if self.rect.bottom >= self.bg.ground_rect.top:
			return True
		return False