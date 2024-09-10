
class FileUtil:

	@staticmethod
	def save_highscore(score):
			file = open("src/highscore.txt", "r")
			print('gamescore - ', score)
			highscore_txt = file.read()
			highscore = int(highscore_txt)
			file.close()
			
			if(score > highscore):
				file = open("src/highscore.txt", "w")
				file.write(str(score))
			file.close()