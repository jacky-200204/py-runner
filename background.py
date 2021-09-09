import pygame

class Background:
	"""Overall class to manage background."""

	def __init__(self, px_runner):
		self.screen = px_runner.screen
		self.screen_rect = self.screen.get_rect()

		self.sky_img = pygame.image.load("graphics/sky.png").convert_alpha()
		self.sky_rect = self.sky_img.get_rect()
		self.sky_rect.midtop = self.screen_rect.midtop

		self.ground_img = pygame.image.load("graphics/ground.png").convert_alpha()
		self.ground_rect = self.ground_img.get_rect()
		self.ground_rect.midtop = self.sky_rect.midbottom

	def draw_bg(self):
		self.screen.blit(self.sky_img, self.sky_rect)
		self.screen.blit(self.ground_img, self.ground_rect)