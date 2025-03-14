# What does this piece of code do?
# Answer:This code simulates rolling two six-sided dice repeatedly until they show the same number, then prints out how many attempts it took.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0#initialize the progress variable
while progress>=0:#while the progress variable is greater than or equal to 0
	progress+=1#increment the progress variable by 1
	first_n = randint(1,6)#generate a random number between 1 and 6
	second_n = randint(1,6)#generate a random number between 1 and 6
	if first_n == second_n:#if the two numbers are the same
		print(progress)#print the number of attempts
		break

