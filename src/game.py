import pygame

from const import *
from board import Board
from config import Config
from fileUtil import FileUtil

class Game:

	def __init__(self, main):
		self.score = 0
		self.board = Board(main)
		self.config = Config()
		self.main = main


	# blit methods 
	
	def show_header(self, surface):
		# Header

		# color
		color = (250, 248, 239)
		# rect
		rect = (0, 0, WIDTH, HEADER)
		# blit
		pygame.draw.rect(surface, color, rect)

		# 2048 Text
		lbl = pygame.font.SysFont('monospace', 200, bold = True).render('2048', 1, self.config.colors[3].color)
		lbl_pos = (25, 0)
		surface.blit(lbl, lbl_pos)

		# Setup Score

		# rect
		rect = (WIDTH - 275, 50, 100, 50)
		# blit
		pygame.draw.rect(surface, self.config.colors[12].color, rect)

		# Write score text

		# rect
		lbl = self.config.font.render('SCORE', 1, self.config.colors[0].color)
		lbl_pos = (WIDTH - 250, 50)
		surface.blit(lbl, lbl_pos)

		# Setup Highscore

		# rect
		rect = (WIDTH - 150, 50, 120, 50)
		# blit
		pygame.draw.rect(surface, self.config.colors[12].color, rect)

		# Highscore text
		lbl = self.config.font.render('HIGHSCORE', 1, self.config.colors[0].color)
		lbl_pos = (WIDTH - 140, 50)
		surface.blit(lbl, lbl_pos)

	
	def show_bg(self, surface):

		# Lower screen

		# color
		color = (205, 193, 180)
		# rect 
		rect = (0, HEADER, WIDTH, HEIGHT - HEADER)
		# blit
		pygame.draw.rect(surface, color, rect)

		# Squares
		
		# color
		color = (187, 173, 160)

		for row in range(4):
			for col in range(4):
				# rect
				rect = (col * SQSIZE, row * SQSIZE + 200, SQSIZE, SQSIZE)
				# blit
				pygame.draw.rect(surface, color, rect, width=10)
		

	def show_pieces(self, surface):
		for r in range(4):
			for c in range(4):

				if self.board.squares[r][c].has_piece():
					piece = self.board.squares[r][c].piece

					# color
					color = self.config.colors[piece.level].color if piece.level < 12 else self.config.colors[11].color
					rect = (c * SQSIZE + 5, r * SQSIZE + 205, SQSIZE - 5, SQSIZE - 5)
					pygame.draw.rect(surface,color,rect)
					
					# text color
					color = (119, 110, 101)
					lbl = self.config.font.render(str(2 ** piece.level), 1, color)
					lbl_pos = (c * SQSIZE + (SQSIZE // 2), r * SQSIZE + (SQSIZE // 2) + HEADER)
					surface.blit(lbl, lbl_pos)

	def update_score(self, surface):
		self.show_header(surface)
		color = (255, 255, 255)
		lbl = self.config.font.render(str(self.score), 1, color)
		lbl_pos = (WIDTH - 225, 70)
		surface.blit(lbl, lbl_pos)

		color = (255, 255, 255)
		lbl = self.config.font.render(str(self.main.highscore), 1, color) if self.score < self.main.highscore else self.config.font.render(str(self.score), 1, color)
		lbl_pos = (WIDTH - 90, 70)
		surface.blit(lbl, lbl_pos)

	def reset(self):
		self.check_highscore()
		self.__init__(self.main)

	def end_game(self):
		self.reset()

	def increase_score(self, inc_amt):
		self.score += inc_amt
		# blit score

	def check_highscore(self):
		if self.score > self.main.highscore:
			FileUtil.save_highscore(self.score)