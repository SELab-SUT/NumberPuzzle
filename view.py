def print_game(game):
	for i in range(3):
		for j in range(3):
			print(game.position[i][j], end='')
		print()


def print_commands():
	print('Enter U to move the empty spot up, R to move it to the right,'
	 ' L to move it to the left, and D to move it down')


def take_input():
	raise NotImplementedError
