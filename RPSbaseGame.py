import random
import time
moves = ["Rock", "Paper","Scissors"]

def GameFlow(): 
	#Intros the game and initiates the flow
	print(moves)
	gameStartIntro = """You're playing rock paper scissors\nPress ENTER to start."""
	print(gameStartIntro)
	startResponse = input()
	PlayerMoves()

def PlayerMoves():
	#Asks for input, checks validity, and responds
	time.sleep(.5)
	print("Enter you move \nPress:\n1 for Rock,\n2 for Paper\n3 for Scissors")
	global moveResponse
	moveResponse = input()	
	moveResponse = int(moveResponse) - 1
	
	if moveResponse == 0:
		CpuMoves()			
	elif moveResponse == 1:
		CpuMoves()
	elif moveResponse == 2:
		CpuMoves()
	else:
		print("Wrong Input!!\n\n\n\n")
		PlayerMoves()

def CpuMoves():
	#Prints moves (CPU & Player)
	time.sleep(.5)
	global cpuMove
	cpuMove = random.randrange(0,3)
	print("You played " + moves[moveResponse])
	print("CPU Played: " + moves[cpuMove])
	CheckForWin()

def CheckForWin():
	#Checks for a winner using if/else
	time.sleep(.5)
	print("\n\n\n")
	if cpuMove == moveResponse:
		print("STALEMATE")
		GameFinish()
	elif cpuMove == 1 and moveResponse == 0:
		print("You LOSE")
		GameFinish()
	elif cpuMove == 2 and moveResponse == 0:
		print("You WIN")
		GameFinish()
	elif cpuMove == 0 and moveResponse == 1:
		print("You WIN")
		GameFinish()
	elif cpuMove == 0 and moveResponse == 2:
		print("You LOSE")
		GameFinish()
	elif cpuMove == 2 and moveResponse == 0:
		print("You LOSE")
		GameFinish()
	elif cpuMove == 2 and moveResponse == 1:
		print("You LOSE")
		GameFinish()
	elif cpuMove == 1 and moveResponse == 2:
		print("You WIN")
		GameFinish()
	else:
		#Added if I missed a move scenario
		print("not in db")
		GameFinish()

def GameFinish():
	#Loops game
	print("\n\n\nPress ENTER to play again")
	playAgain = input()
	PlayerMoves()

GameFlow()