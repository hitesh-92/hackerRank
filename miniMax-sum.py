"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers. 
For example, arr=[1,3,5,7,9]
Our minimum sum is 1+3+5+7 = 16 and our maximum is 3+5+7+9 = 24
Print:
16 24
"""

def miniMaxSum(arr):

	maxi = 0
	mini = 0

	for i in range(len(arr)):


		# newArray = [x for x in arr if x != arr[i] ]
		#fixed
		newArray = [x for x in arr ]
		del newArray[i]

		print('new',newArray)
		result = 0
		for n in newArray: result += n
		
		print(result)

		if (mini == 0 & maxi == 0):
			mini = result
			maxi = result

		if(result < mini): mini = result
		if(result > maxi): maxi = result

	print(mini, maxi)

miniMaxSum([5,5,5,5,5])


#loop through array
#loop again to go over every number but omit x number in sum
#if sum is higher set as new highest


