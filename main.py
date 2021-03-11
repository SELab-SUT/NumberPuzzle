from logic import Game
from view import *

def run():
	game = Game()
	print_commands()
	while not game.has_finished():
		print_game(game)
		input_xy = take_input()
		game.move(input_xy)
	print("Game over, You won!")


if __name__=='__main__':
	run()
