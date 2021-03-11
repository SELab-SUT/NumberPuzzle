from logic import Game
from view import *

def run():
	game = Game()
	print_commands()
	while not game.has_finished():
		print_game(game)
		game.move(take_input())
	print_game(game)
	print_win()

if __name__=='__main__':
	run()
