import pygame
import os

from color import Color
from sound import Sound

class Config:
	
	def __init__(self):
		self.colors = []
		self._add_themes()
		self.font = pygame.font.SysFont('monospace', 18, bold = True)
		self.move_sound = Sound(
			os.path.join('src/assets/move.wav')
		)

	def _add_themes(self):
		color_empty = Color(204, 192, 179)
		color_2 = Color(238, 228, 218)
		color_4 = Color(237, 224, 200)
		color_8 = Color(242, 177, 121)
		color_16 = Color(245, 149, 99)
		color_32 = Color(246, 124, 95)
		color_64 = Color(246, 94, 59)
		color_128 = Color(237, 207, 114)
		color_256 = Color(237, 204, 97)
		color_512 = Color(237, 200, 80)
		color_1024 = Color(237, 197, 63)
		color_2048 = Color(237, 194, 46)
		color_other = Color(249, 249, 249)
		color_bg = Color(205, 193, 180)

		self.colors = [color_2, color_4, color_8, color_16, color_32, color_64, color_128, color_256, color_512, color_1024, color_2048, color_other, color_bg]