from logic import Game
from view import *


def run():
	game = Game([[1, 2, 3], [4, 5, 6], [7, '*', 8]])
	while True:
		print_game(game)
		print_commands()
		game.move(take_input())


if __name__=='__main__':
	run()
