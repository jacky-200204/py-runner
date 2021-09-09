import pygame
import sys

from settings import Settings
from background import Background
from player import Player
from obstacle import Obstacle


class Runner:

	def __init__(self):
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,
			 self.settings.screen_height))
		pygame.display.set_caption("Pixel Runner")
		self.clock = pygame.time.Clock()

		self.bg = Background(self)
		self.player = Player(self)

		# Obstacle Group
		self.obstacles = pygame.sprite.Group()
		snail = Obstacle(self)
		self.obstacles.add(snail)

	def run_game(self):
		while True:
				self._check_events()
				self.obstacles.update()
				self.player.update()
				self._update_screen()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and self.player.check_bottom():
					self.player.jump()

	def _update_screen(self):
		self.bg.draw_bg()
		self.player.draw()
		self.obstacles.draw(self.screen)
		pygame.display.flip()
		self.clock.tick(30)


if __name__ == "__main__":
	runner = Runner()
	runner.run_game()