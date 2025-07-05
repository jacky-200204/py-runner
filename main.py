import pygame
import sys
import random
from time import sleep

from settings import Settings
from background import Background
from player import Player
from obstacle import Obstacle
from game_stats import Stats
from score_board import Scoreboard


class Runner:

	def __init__(self):
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,
			 self.settings.screen_height))
		pygame.display.set_caption("Pixel Runner")
		self.clock = pygame.time.Clock()

		self.stats = Stats()
		self.bg = Background(self)
		self.player = Player(self)

		# Obstacle Group
		self.obstacles = pygame.sprite.Group()

		# UserEvent
		self.obstacle_timer = pygame.USEREVENT + 1
		pygame.time.set_timer(self.obstacle_timer, 1500)

		self.score_event = pygame.USEREVENT + 2
		pygame.time.set_timer(self.score_event, 500)

		# Scoreboard
		self.sb = Scoreboard(self)

	def run_game(self):
		while True:
				self._check_events()
				if self.stats.game_active:
					self._update_obstacles()
					self.player.update()
					self._level_up_game()
				self._update_screen()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and self.player.check_bottom():
					self.player.jump()
				if event.key == pygame.K_SPACE and not self.stats.game_active:
					self.stats.game_active = True
					self.stats.reset_stats()
			elif event.type == self.obstacle_timer and self.stats.game_active:
				self._create_obstacle()
			elif event.type == self.score_event and self.stats.game_active:
				self.sb.give_score()
				self.sb.prep_score()

	def _update_screen(self):
		if self.stats.game_active:
			self.bg.draw_bg()
			self.player.draw()
			self.obstacles.draw(self.screen)

		self.sb.draw_score()
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
				self.stats.game_active = False
				self.obstacles.empty()
				self.player.down_player()
				self._draw_end_screen()

	def _draw_end_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.bg.draw_player()

	def _level_up_game(self):
		pass

if __name__ == "__main__":
	runner = Runner()
	runner.run_game()