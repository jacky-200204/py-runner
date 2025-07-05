import random


import pygame
from pygame.sprite import Sprite

class Obstacle(Sprite):
	"""Overall class to manage the obstacles."""

	def __init__(self, px_runner, ob_type):
		super().__init__()
		self.bg = px_runner.bg
		self.settings = px_runner.settings

		snail_image1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
		snail_image2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
		self.snail_list = [snail_image1, snail_image2]
		self.snail_index = 0
		self.fly_index = 0

		fly_img1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
		fly_img2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
		self.fly_list = [fly_img1, fly_img2]

		self.initialize_img(ob_type)
		if ob_type == "snail":
			self.rect = self.image.get_rect(centerx=random.randint(900, 1100))
			self.rect.bottom = self.bg.ground_rect.top
		else:
			self.rect = self.image.get_rect(centerx=random.randint(900, 1100))
			self.rect.bottom = self.bg.sky_rect.centery

	def initialize_img(self, ob_type):
		if ob_type == "snail":
			self.image = self.snail_list[int(self.snail_index)]
		else:
			self.image = self.fly_list[int(self.fly_index)]

	def _move_obstacle(self):
		self.rect.x -= self.settings.obstacle_speed

	def destroy(self):
		self.kill()

	def _animate_obstacles(self):
		self.snail_index += 0.1
		if self.snail_index >= len(self.snail_list):
			self.snail_index = 0

		self.fly_index += 0.3
		if self.fly_index >= len(self.fly_list):
			self.fly_index = 0

	def update(self):
		self._move_obstacle()
		self._animate_obstacles()
		if self.rect.bottom == self.bg.ground_rect.top:
			self.initialize_img("snail")
		else:
			self.initialize_img("fly")


