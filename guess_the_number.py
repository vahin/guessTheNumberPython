import random
import os
import sys

os.system("cls")
print("====GUESS THE NUMBER====")
print("\nHelp: The game will decide a number between 1 to 10 and you have to try to guess the number,\nyou have 5 chances\nIf you want to quit the game, enter 'exit'")
print("\nGame developer: Vahin Sharma")
min_number = 1 # Set this to whatever you want
max_number = 10 # Set this to whatever you want
tries = 5
answer = random.randint(min_number, max_number)
flag = False
anotherFlag = True
while anotherFlag:
	print("Guess a number between {} to {}\n".format(min_number, max_number))
	print("Chances:",tries,"\n")
	flag = False
	while not flag:
		guess = input()
		if(guess == "exit"):
			quit()
		else:
			try:
				guess = int(guess)
			except:
				print("Invalid input!")
				continue
			if guess == answer:
				print("\nCongratulations! You Win!")
				quit()
			elif guess > answer:
				tries -= 1
				print("\nGuess lower\n")
				print("Chances:",tries,"\n")
			elif guess < answer:
				tries -= 1
				print("\nGuess higher\n")
				print("Chances:",tries,"\n")
			if(tries == 0):
				print("You have ran out of chances, better luck next time!")
				quit()
