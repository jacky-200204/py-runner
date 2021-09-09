import pygame

class Background:
	"""Overall class to manage background."""

	def __init__(self, px_runner):
		self.screen = px_runner.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = px_runner.settings

		self.sky_img = pygame.image.load("graphics/sky.png").convert_alpha()
		self.sky_rect = self.sky_img.get_rect()
		self.sky_rect.midtop = self.screen_rect.midtop

		self.ground_img = pygame.image.load("graphics/ground.png").convert_alpha()
		self.ground_rect = self.ground_img.get_rect()
		self.ground_rect.midtop = self.sky_rect.midbottom

		player_stop = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
		self.player_stop = pygame.transform.scale2x(player_stop)
		self.player_rect = self.player_stop.get_rect(center=self.screen_rect.center)

		self.game_logo = pygame.image.load("graphics/logo.png").convert_alpha()
		self.logo_rect = self.game_logo.get_rect(centerx=self.screen_rect.centerx)
		self.logo_rect.y = 20

		self.again_msg = pygame.image.load("graphics/again_msg.png").convert_alpha()
		self.msg_rect = self.again_msg.get_rect(centerx=self.screen_rect.centerx)
		self.msg_rect.y = 300

	def draw_bg(self):
		self.screen.blit(self.sky_img, self.sky_rect)
		self.screen.blit(self.ground_img, self.ground_rect)

	def draw_player(self):
		self.screen.blit(self.player_stop, self.player_rect)
		self.screen.blit(self.game_logo, self.logo_rect)
		self.screen.blit(self.again_msg, self.msg_rect)