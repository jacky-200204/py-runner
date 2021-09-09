import pygame
from pygame.sprite import Sprite

class Obstacle(Sprite):
	"""Overall class to manage the obstacles."""

	def __init__(self, px_runner):
		super().__init__()
		self.bg = px_runner.bg

		self.image = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
		self.rect = self.image.get_rect(centerx=700)
		self.rect.bottom = self.bg.ground_rect.top

	def _walk_snail(self):
		self.rect.x -= 8
		if self.rect.x <= -100:
			self.rect.x = 900

	def update(self):
		self._walk_snail()
