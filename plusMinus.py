"""
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.
For example, given the array: arr = [1, 1, 0,- 1, -1]
here are elements, two positive, two negative and one zero. 
Their ratios would be:
	2/5 = 0.400000
	2/5 = 0.400000
	1/5 = 0.200000
"""

def plusMinus(arr):

	positive = 0
	negative = 0
	zero = 0

	for i in arr:
		if i == 0: zero += 1
		elif i > 0: positive += 1
		else: negative += 1

	first = format(float(positive / len(arr)), '.6f')
	second = format(float(negative / len(arr)), '.6f')
	third = format(float(zero / len(arr)), '.6f')

	print(first)
	print(second)
	print(third)
	return


arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)