from logic import Game
from view import *

def run():
	print_commands()
	replay = True
	while replay:
		game = Game()
		while not game.has_finished():
			print_game(game)
			try:
				game.move(take_input())
			except Exception as e:
				print("Error:", e)
		print_game(game)
		replay = print_win_and_get_replay()

if __name__=='__main__':
	run()
