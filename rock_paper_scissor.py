import random

user = input("Choose between ROCK, PAPER & SCISSOR = ")
var = ["ROCK","PAPER","SCISSOR"]
comp = random.choice(var)

print("Your input is ",user)

print("Computer input is ",comp)

if ((user == 'ROCK' and comp == 'SCISSOR') or (user == 'SCISSOR' and comp == 'ROCK')):
	print("ROCK Wins .....")

elif ((user == 'ROCK' and comp == 'PAPER') or (user == 'PAPER' and comp == 'ROCK')):
	print("PAPER Wins .....")

elif ((user == 'SCISSOR' and comp == 'PAPER') or (user == 'PAPER' and comp == 'SCISSOR')):
	print("SCISSOR Wins .....")

else:
	print("Both are same, please try again.")