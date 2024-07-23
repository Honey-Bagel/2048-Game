import random

from const import *
from piece import Piece
from square import Square
from eDirection import Direction


class Board:

	def __init__(self, main):
		self.squares = [[0, 0, 0, 0] for col in range(4)]
		self.open_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

		self._create()
		self.add_piece()
		self.add_piece()
		self.main = main
		self.b_should_add_piece = True

	def _create(self):
		for r in range(4):
			for c in range(4):
				self.squares[r][c] = Square(r, c)

	def add_piece(self):
		loc = self.open_spaces[random.randrange(0, self.open_spaces.__len__())]
		r = loc // 4
		c = loc % 4
		self.squares[r][c] = Square(r, c, Piece(1))
		self.open_spaces.remove(loc)

	def has_open_spot(self):
		return self.open_spaces.__len__() > 0
		
	def should_add_piece(self):
		return self.b_should_add_piece

	def move(self, edirection):
		direction = None
		self.b_should_add_piece = False
		if edirection == Direction.DOWN:
			direction = (0, -1)
			for r in range(2, -1, -1):
				for c in range(4):
					lcl_r = r
					square = self.squares[r][c]
					# if next square is empty move to that square
					while (lcl_r+1) <= 3:
						if square.has_piece() and self.squares[lcl_r+1][c].is_empty():
							piece = square.piece
							self.squares[lcl_r][c] = Square(lcl_r, c)
							self.open_spaces.append((lcl_r * 4) + c)
							self.open_spaces.remove(((lcl_r +1) * 4) + c)
							self.squares[lcl_r+1][c].piece = piece
							self.b_should_add_piece = True
						# if next piece the same, upgrade that piece and combine them
						elif self.squares[lcl_r+1][c].has_piece() and square.has_piece() and square.piece.level == self.squares[lcl_r+1][c].piece.level:
							self.squares[lcl_r][c] = Square(lcl_r, c)
							self.open_spaces.append((lcl_r * 4) + c)
							# self.open_spaces.remove((lcl_r + 1) * 4 + c)
							self.squares[lcl_r+1][c].piece.inc_level()
							self.main.update_score(2 ** self.squares[lcl_r+1][c].piece.get_level())
							self.b_should_add_piece = True
						lcl_r += 1

		elif edirection == Direction.LEFT:
			direction = (-1, 0)
			for c in range(1,4):
				for r in range(4):
					lcl_c = c
					square = self.squares[r][c]
					# if next squares is empty move to that square
					while (lcl_c - 1) >= 0:
						if square.has_piece() and self.squares[r][lcl_c - 1].is_empty():
							piece = square.piece
							self.squares[r][lcl_c] = Square(r, lcl_c)
							self.open_spaces.append((r * 4) + lcl_c)
							self.open_spaces.remove((r * 4) + lcl_c - 1)
							self.squares[r][lcl_c - 1].piece = piece
							self.b_should_add_piece = True
						# if next piece is the same, upgrade that piece and combine them
						elif self.squares[r][lcl_c-1].has_piece() and square.has_piece() and square.piece.level == self.squares[r][lcl_c-1].piece.level:
							self.squares[r][lcl_c] = Square(r, lcl_c)
							self.open_spaces.append((r * 4) + lcl_c)
							# self.open_spaces.remove((r * 4) + lcl_c - 1)
							self.squares[r][lcl_c-1].piece.inc_level()
							self.main.update_score(2 ** self.squares[r][lcl_c-1].piece.get_level())
							self.b_should_add_piece = True
						lcl_c -= 1

		elif edirection == Direction.RIGHT:
			direction = (1, 0)
			for c in range(2, -1, -1):
				for r in range(4):
					lcl_c = c
					square = self.squares[r][c]
					# if next square is empty move to that square
					while(lcl_c+1) <= 3:
						if square.has_piece() and self.squares[r][lcl_c+1].is_empty():
							piece = square.piece
							self.squares[r][lcl_c] = Square(r, lcl_c)
							self.open_spaces.append((r * 4) + lcl_c)
							self.open_spaces.remove((r * 4) + lcl_c + 1)
							self.squares[r][lcl_c+1].piece = piece
							self.b_should_add_piece = True
						# if next piece is the same, upgrade that piece and combine them
						elif self.squares[r][lcl_c+1].has_piece() and square.has_piece() and square.piece.level == self.squares[r][lcl_c+1].piece.level:
							self.squares[r][lcl_c] = Square(r, lcl_c)
							self.open_spaces.append((r * 4) + lcl_c)
							# self.open_spaces.remove((r * 4) + lcl_c + 1)
							self.squares[r][lcl_c+1].piece.inc_level()
							self.main.update_score(2 ** self.squares[r][lcl_c+1].piece.get_level())
							self.b_should_add_piece = True
						lcl_c += 1

		elif edirection == Direction.UP:
			direction = (0, 1)
			for r in range(1, 4):
				for c in range(4):
					lcl_r = r
					square = self.squares[r][c]
					# if next square is empty move to that square
					while(lcl_r - 1) >= 0:
						if square.has_piece() and self.squares[lcl_r-1][c].is_empty():
							piece = square.piece
							self.squares[lcl_r][c] = Square(lcl_r, c)
							self.open_spaces.append((lcl_r * 4) + c)
							self.open_spaces.remove(((lcl_r-1) * 4) + c)
							self.squares[lcl_r-1][c].piece = piece
							self.b_should_add_piece = True
						# if next piece is thhe same, upgrade that piece and combine them
						elif self.squares[lcl_r-1][c].has_piece() and square.has_piece() and square.piece.level == self.squares[lcl_r-1][c].piece.level:
							self.squares[lcl_r][c] = Square(lcl_r, c)
							self.open_spaces.append((lcl_r * 4) + c)
							# self.open_spaces.remove(((lcl_r-1) * 4) + c)
							self.squares[lcl_r-1][c].piece.inc_level()
							self.main.update_score(2 ** self.squares[lcl_r-1][c].piece.get_level())
							self.b_should_add_piece = True
						lcl_r -= 1

	def check_spaces(self):
		for r in range(4):
			for c in range(4):
				square = self.squares[r][c]
				sqr_idx = ((square.row * 4) + square.col)
				if square.has_piece():
					if self.open_spaces.index(sqr_idx) != -1:
						self.open_spaces.remove(sqr_idx)
				else:
					if self.open_spaces.index(sqr_idx) == -1:
						self.open_spaces.append(sqr_idx)

	def move_piece(self, square, dir):
		# (1, 0) right 
		# (-1, 0) left
		# (0, 1) up 
		# (0, -1) down
		for r in range(2, -1, -1):
				for c in range(4):
					lcl_r = r
					square = self.squares[r][c]
					# if next square is empty move to that square
					while (lcl_r+1) <= 3:
						if square.has_piece() and self.squares[lcl_r+1][c].is_empty():
							piece = square.piece
							self.squares[lcl_r][c] = Square(lcl_r, c)
							self.open_spaces.append((lcl_r * 4) + c)
							self.squares[lcl_r + dir[0]][c + dir[1]].piece = piece
						# if next piece the same, upgrade that piece and combine them
						elif self.squares[lcl_r+1][c].has_piece() and square.has_piece() and square.piece.level == self.squares[lcl_r+1][c].piece.level:
							self.squares[lcl_r][c] = Square(lcl_r, c)
							self.open_spaces.append((lcl_r * 4) + c)
							self.sq

	def getEdge(self, sqr, direction):
		r = sqr.row
		c = sqr.col
		if direction == Direction.DOWN:
			pass
		elif direction == Direction.LEFT:
			pass
		elif direction == Direction.RIGHT:
			pass
		elif direction == Direction.UP:
			pass
