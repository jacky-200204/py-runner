import random


import pygame
from pygame.sprite import Sprite

class Obstacle(Sprite):
	"""Overall class to manage the obstacles."""

	def __init__(self, px_runner, ob_type):
		super().__init__()
		self.bg = px_runner.bg

		if ob_type == "snail":
			self.image = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
			self.rect = self.image.get_rect(centerx=random.randint(900, 1100))
			self.rect.bottom = self.bg.ground_rect.top
		else:
			self.image = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
			self.rect = self.image.get_rect(centerx=random.randint(900, 1100))
			self.rect.bottom = self.bg.sky_rect.centery

	def _move_obstacle(self):
		self.rect.x -= 8

	def destroy(self):
		self.kill()

	def update(self):
		self._move_obstacle()

