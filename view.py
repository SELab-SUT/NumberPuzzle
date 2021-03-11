def print_game(game):
	for i in range(3):
		for j in range(3):
			print(game.position[i][j], end='')
		print()


def print_commands():
	print('Enter U to move a block up, R to move it to the right,'
	 ' L to move it to the left, and D to move it down')


def take_input():
	action = input().upper()
	if action not in ['U', 'R', 'L', 'D']:
		raise Exception('Invalid input')
	return action
