import pygame
import sys
import random
from time import sleep

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
		# snail = Obstacle(self)
		# self.obstacles.add(snail)
		self.obstacle_timer = pygame.USEREVENT + 1
		pygame.time.set_timer(self.obstacle_timer, 1500)

	def run_game(self):
		while True:
				self._check_events()
				self._update_obstacles()
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
			elif event.type == self.obstacle_timer:
				self._create_obstacle()

	def _update_screen(self):
		self.bg.draw_bg()
		self.player.draw()
		self.obstacles.draw(self.screen)
		pygame.display.flip()
		self.clock.tick(30)

	def _create_obstacle(self):
		obstacle_type = random.choice(("snail", "snail", "fly", "snail"))
		obstacle = Obstacle(self, obstacle_type)
		self.obstacles.add(obstacle)

	def _update_obstacles(self):
		self.obstacles.update()
		for obstacle in self.obstacles.sprites():
			if obstacle.rect.x <= -100:
				obstacle.destroy()
			if obstacle.rect.colliderect(self.player.rect):
				self.obstacles.empty()
				self.stats.game_active = False
				sleep(0.5)


if __name__ == "__main__":
	runner = Runner()
	runner.run_game()