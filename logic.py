class Game:
	def __init__(self, position):
		self.position = position.copy()

	def move(self, move_type):
		raise NotImplementedError

	def __check_validity(self, move_type):
		raise NotImplementedError

	def __check_finished(self):
		raise NotImplementedError
