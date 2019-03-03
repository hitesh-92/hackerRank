"""
Consider a staircase of size n = 4:
   #
  ##
 ###
####

Write a program that prints a staircase of size n
"""

def staircase(n):

	space = n-1
	stair = 1

	for i in range(n):
		seq = ''
		for s in range(space):
			seq += ' '
		for s in range(stair):
			seq += '#'

		space -= 1
		stair += 1

		print(seq)

	return


staircase(5)