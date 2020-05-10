import random
moves = ["Rock", "Paper","Scissors"]
print(type(moves))
print(moves)



def GameFlow(): 
	gameStartIntro = """You're playing rock paper scissors\nPress ENTER to start."""
	print(gameStartIntro)
	startResponse = input()
	FirstStage()

def FirstStage():
	print("Enter you move \nPress:\n1 for Rock,\n2 for Paper\n3 for Scissors")
	moveResponse = input()
	global intMove
	intMove = int(moveResponse) - 1
	
	if int(moveResponse) == 1:
		print("You played " + moves[int(moveResponse) - 1])
		SecondStage()	
		
	elif int(moveResponse) == 2:
		print("You played " + moves[int(moveResponse) - 1])
		SecondStage()

	elif int(moveResponse) == 3:
		print("You played " + moves[int(moveResponse) - 1])
		SecondStage()
	
	else:
		print("\Wrong Input!!\n\n\n\n")
		FirstStage()

def SecondStage():
	global cpuMove
	cpuMove = random.randrange(0,3)
	print("CPU Played: " + moves[cpuMove])
	GameFinish()

def GameFinish():
	if cpuMove == 0 and intMove == 1:
		print("You WIN")
	elif cpu


GameFlow()