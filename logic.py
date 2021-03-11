class Game:
	def __init__(self):
		self.__width = 3
		self.__height = 3
		self.position = [[8, 3, 4],
						 [2, 1, 7],
						 [5, 6, '*']]
		self.__empty_position = self.__find_empty_place();

	def move(self, move_position):
		raise NotImplementedError

	def __check_validity(self, move_position):
		raise NotImplementedError

	def __find_empty_place(self):
		for i in range(self.__height):
			for j in range(self.__width):
				if self.position[i][j] == '*':
					return (i, j)

		raise Exception("There is no empty place in the board.")

	def has_finished(self):
		# TODO: Return state of game based on the board
		return False
