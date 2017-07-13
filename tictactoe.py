import random
import sys
import os
import re

def diplay_title():
	print("\t-------------------")
	print("\t****TIC TAC TOE****")
	print("\t-------------------")

def display_board(gameboard):
	print("Board Current State")
	for k,v in game_board.items() :
		if k <= 3:
			print("\t"+v,end ='|')
		elif k > 3 and k <= 6 :
			print("\t"+v,end='|')
		else:
			print("\t"+v,end='|')
	
		if k == 3:
			print("\n")
		elif k == 6:
			print("\n")
		else :
			continue

def game_won(gameboard,player):
	if ((gameboard[1] == player and gameboard[2]== player and gameboard[3] == player) or \
		(gameboard[4] == player and gameboard[5]== player and gameboard[6] == player) or \
		(gameboard[7] == player and gameboard[8]== player and gameboard[9] == player) or \
		(gameboard[1] == player and gameboard[4]== player and gameboard[7] == player) or \
		(gameboard[2] == player and gameboard[5]== player and gameboard[8] == player) or \
		(gameboard[3] == player and gameboard[6]== player and gameboard[9] == player) or \
		(gameboard[1] == player and gameboard[5]== player and gameboard[9] == player) or \
		(gameboard[3] == player and gameboard[5]== player and gameboard[7] == player)):
		return 1
	else:
		return 0

def decide_position(board,computer,human,free_postions):
	win_prob = {1:3,2:2,3:3,4:2,5:4,6:2,7:3,8:2,9:3}
	for pos in free_postions:
		board[int(pos)] = computer
		if game_won(gameboard=board,player=computer):
			board[int(pos)] = '-'
			return pos
		board[int(pos)] = human
		if game_won(gameboard=board,player=human):
			return pos
		board[int(pos)] = '-'

	high_prob = sorted(free_postions,key =win_prob.get)

	return high_prob[-1:][0]

def init_game():
	os.system("cls")
	
	global hu_player_symbol,comp_player_symbol,game_board

	hu_player_symbol = input("Enter Symbol (O or X) :")
	comp_player_symbol =""
	
	if hu_player_symbol == "X":
		comp_player_symbol = "O"
	else:
		comp_player_symbol = "X"
	
	game_board = {1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'}

	print ("Your Symbol:" + hu_player_symbol+"\nComputer Symbol:" + comp_player_symbol)
	display_board(gameboard = game_board)

def reset():
	game_cont = input("New Game (Y/N)?")
	if game_cont == "Y":
		init_game()
		return 1
	else:
		return 0

if __name__ == '__main__':

	hu_player_symbol =""
	comp_player_symbol=""
	game_board={}
	
	init_game()
	
	while True:
		try:
			
			print("\nYour Turn...")
			player_position = input("\nPlace Your Mark:")
			if int(player_position) in game_board.keys() and game_board[int(player_position)] == '-':
				game_board[int(player_position)] = hu_player_symbol
				display_board(gameboard = game_board)
				if game_won(gameboard = game_board,player = hu_player_symbol):
					print("\n\t!!!!!Congratulations You have  Won the Game!!!!!")
					if reset():
						continue
					else:
						break
			else :
				print("ALERT : Give a value Between 0-9 which is empty")
				continue
				
			print("\n\nComputers Turn...")
			empty_places = []
			for k,v in game_board.items():
				if v == '-':
					empty_places.append(k)
			if empty_places :
				computer_position = decide_position(board=game_board,computer=comp_player_symbol,human=hu_player_symbol,free_postions=empty_places)
				game_board[int(computer_position)] = comp_player_symbol
				display_board(gameboard = game_board)
				if game_won(gameboard = game_board,player = comp_player_symbol):
					print("\n\t!!!!The Computer Has Won!!!!")
					if reset():
						continue
					else:
						break
			else:
				print("Game is a Draw")
				if reset():
					continue
				else:
					break
			continue
			
		except KeyboardInterrupt:
			break
