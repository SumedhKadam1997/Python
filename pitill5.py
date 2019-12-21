import math
roundVal = int(input("How many digits of pi do you want after decimal?")) 

def CalculatePi(roundVal):

		somepi = round(math.pi,roundVal);
		return somepi

print(CalculatePi(roundVal))