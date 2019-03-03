"""
arr1= [1, 2, 3]
arr2= [4, 5, 6]
arr3= [9, 8, 9]

The left-to-right diagonal: 1+5+9 = 15
The right-to-left diagonal: 3+5+9 = 17
Their absolute difference: 15-17 = 2
"""

def diagonalDifference(arr):

	def leftPass():
		result = 0
		size = len(arr[0]) - 1
		for i in range(len(arr)):
			result += arr[i][size]
			size -= 1
		return result

	def rightPass():
		result = 0
		size = 0
		for i in range(len(arr)):
			result += arr[i][size]
			size += 1
		return result



	return abs( leftPass() - rightPass() )

	


# arr1=[11, 2, 4]
# arr2=[4, 5, 6]
# arr3=[10, 8, -12]
arr = [ [11, 2, 4], [4, 5, 6], [10, 8, -12] ]

x = diagonalDifference(arr)

print(x)