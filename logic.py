class Game:
	def __init__(self):
		self.__cols = 3
		self.__rows = 3
		self.position = [[8, 3, 4],
						 [2, 1, 7],
						 [5, 6, '*']]
		self.__empty_position = self.__find_empty_place();

	def move(self, move_type):
		move_position = self.__get_moving_tile(move_type)
		self.__check_validity(move_position)
		empty_x, empty_y = self.__empty_position
		move_x, move_y = move_position
		self.position[move_x][move_y], self.position[empty_x][empty_y] = self.position[empty_x][empty_y], self.position[move_x][move_y]
		self.__empty_position = move_position

	def __get_moving_tile(self, move_type):
		next_tile_distance = {'L': (0, 1), 'U': (1, 0), 'R': (0, -1), 'D': (-1, 0)}
		return (self.__empty_position[0] + next_tile_distance[move_type][0], self.__empty_position[1] + next_tile_distance[move_type][1])

	def __check_validity(self, move_position):
		if move_position[0] < 0 or move_position[1] < 0 or move_position[0] >= self.__rows or move_position[1] >= self.__cols:
			raise Exception("Moving tile position will be outside of the board.")

	def __find_empty_place(self):
		for i in range(self.__rows):
			for j in range(self.__cols):
				if self.position[i][j] == '*':
					return (i, j)

		raise Exception("There is no empty place in the board.")

	def has_finished(self):
		# TODO: Return state of game based on the board
		return False
