import pygame
import sys

from const import *
from game import Game
from eDirection import Direction
from fileUtil import FileUtil
from square import Square
from piece import Piece

class Main:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
		pygame.display.set_caption('2048')
		self.game = Game(self)
		self.can_move = True

		self.highscore = 0
		self.load_highscore()

	def load_highscore(self):
		try:
			with open("src/highscore.txt", 'x') as file:
				file.write("0")
				file.close()
			
		except FileExistsError:
			print("File already exists")

		h_score_f = open("src/highscore.txt")
		highscore_txt = h_score_f.read()
		h_score_f.close()
		self.highscore = int(highscore_txt)
	
	def mainloop(self):
		screen = self.screen
		game = self.game
		board = self.game.board

		game.show_header(screen)
		game.update_score(screen)

		while True:
			game.show_bg(screen)
			game.show_pieces(screen)
			#game.show_message(screen, "Game Over\nPress 'r' to reset")


			for event in pygame.event.get():
				
				if event.type == pygame.KEYDOWN:
					# left arrow or a key
				
					if self.can_move:
						key_pressed = False
						if event.key == pygame.K_LEFT or event.key == pygame.K_a:
							board.move(Direction.LEFT)
							key_pressed = True

						# down arrow or s key
						if event.key == pygame.K_DOWN or event.key == pygame.K_s:
							board.move(Direction.DOWN)
							key_pressed = True

						# right arrow or d key
						if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
							board.move(Direction.RIGHT)
							key_pressed = True

						# up arrow or w key
						if event.key == pygame.K_UP or event.key == pygame.K_w:
							board.move(Direction.UP)
							key_pressed = True

						if key_pressed:
							self.can_move = False
							game.show_bg(screen)
							game.show_pieces(screen)

							if board.has_open_spot() and board.should_add_piece():
								board.add_piece()
								self.can_move = True
							# print(game.board.open_spaces)
							for i in range(len(game.board.squares)):
								for j in range(len(game.board.squares[0])):
									tempPiece = game.board.squares[i][j].piece
									if(tempPiece):
										print(2 ** tempPiece.level, end='')
										print(' ', end='')
									else:
										print(0, end='')
										print(' ', end='')
								print()
							print()
							self.can_move = True
							if not board.has_open_spot():
								game.reset()
								game = self.game
								board = self.game.board
								self.load_highscore()
								game.update_score(self.screen)

					if event.key == pygame.K_r:
						game.reset()
						game = self.game
						board = self.game.board
						self.load_highscore()
						game.update_score(self.screen)
					

				# Quit
				if event.type == pygame.QUIT:
					print('quit')
					self.quit()



			pygame.display.update()

	def quit(self):
		FileUtil.save_highscore(self.game.score)
		pygame.quit()
		sys.exit()

	def update_score(self, score):
		self.game.increase_score(score)
		self.game.update_score(self.screen)







main = Main()
main.mainloop()