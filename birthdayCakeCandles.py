#if your niece is turning 4 years old, and the cake will have 4 candles of height 4,4,1,3
#she will be able to blow out 2 candles successfully
#since the tallest candles are of height 4 and there are 2 such candles. 

def birthdayCakeCandles(ar):
	tallest = max(ar)
	amount = [x for x in ar if x == tallest]
	return len(amount)

x=birthdayCakeCandles([3, 2, 1, 3])
print(x)