import pygame
import sys

from const import *
from game import Game
from eDirection import Direction

class Main:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
		pygame.display.set_caption('2048')
		self.game = Game(self)

	
	def mainloop(self):
		screen = self.screen
		game = self.game
		board = self.game.board

		game.show_header(screen)
		game.update_score(screen)

		while True:
			game.show_bg(screen)
			game.show_pieces(screen)


			for event in pygame.event.get():
				
				if event.type == pygame.KEYDOWN:
					# left arrow or a key
					if event.key == pygame.K_LEFT or event.key == pygame.K_a:
						board.move(Direction.LEFT)
						print('l')

					# down arrow or s key
					if event.key == pygame.K_DOWN or event.key == pygame.K_s:
						board.move(Direction.DOWN)

					# right arrow or d key
					if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
						board.move(Direction.RIGHT)
						print('r')

					# up arrow or w key
					if event.key == pygame.K_UP or event.key == pygame.K_w:
						board.move(Direction.UP)
						print('u')

					game.show_bg(screen)
					game.show_pieces(screen)

					if board.has_open_spot():
						board.add_piece()
					else:
						game.end_game()

					if event.key == pygame.K_r:
						game.reset()
						game = self.game
						board = self.game.board
					

				# Quit
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()



			pygame.display.update()

	def update_score(self, score):
		self.game.increase_score(score)
		self.game.update_score(self.screen)







main = Main()
main.mainloop()