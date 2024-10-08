
class Square:

	def __init__(self, row, col, piece=None):
		self.row = row
		self.col = col
		self.piece = piece

	def __eq__(self, other):
		return self.row == other.row and self.col == other.col
	
	def has_piece(self):
		return self.piece != None
	
	def is_empty(self):
		return self.piece == None
	
	def get_piece(self):
		return self.piece
	

	@staticmethod
	def in_range(*args):
		for arg in args:
			if arg < 0 or arg > 3:
				return False
		
		return True