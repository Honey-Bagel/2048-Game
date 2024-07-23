
class FileUtil:

	@staticmethod
	def save_highscore(score):
			file = open("src/highscore.txt", "w")
			print('gamescore - ', score)
			file.write(str(score))
			file.close()