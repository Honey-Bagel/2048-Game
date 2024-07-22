import os

class Piece:

	def __init__(self, level):
		self.level = level

	def __eq__(self, other):
		if other is None:
			return False
		return self.level == other.level
	
	def inc_level(self):
		self.level += 1

	def get_level(self):
		return self.level