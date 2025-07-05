import pygame


class Scoreboard:
	"""Overall class to manage scores."""

	def __init__(self, px_runner):
		self.screen = px_runner.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = px_runner.settings
		self.stats = px_runner.stats

		self.font = pygame.font.Font("pixel_font.ttf", 48)
		self.prep_score()

	def prep_score(self):
		self.score = self.font.render(f"Score: {int(self.stats.score)}", False, "Green")
		self.score_rect = self.score.get_rect()
		self.score_rect.top = self.screen_rect.top + 20
		self.score_rect.right = self.screen_rect.right - 20

	def draw_score(self):
		self.screen.blit(self.score, self.score_rect)

	def give_score(self):
		self.stats.score += self.settings.points