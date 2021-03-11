class Game:
	def __init__(self):
		self.position = []
		self.__empty_position = self.__find_empty_place();

	def move(self, move_position):
		raise NotImplementedError

	def __check_validity(self, move_position):
		raise NotImplementedError

	def __find_empty_place(self):
		for i in range(len(self.position)):
			for j in range(len(self.position[i])):
				if self.position[i][j] == '*':
					return (i, j)

		raise Exception("There is no empty place in the board.")

	def has_finished(self):
		raise NotImplementedError
