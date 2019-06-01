import os
os.system('cls' if os.name == 'nt' else 'clear')
# nodemon --exec python3 test.py

#repeat string until it has n letters
#find number of occurrences of 'a'

def repeatedString(s, n):
    #find number of 'a' in current length
    #multiply til n
    length = len(s)
    a = s.count('a')

    total =  int(n / length)
    remainder = int(n % length)

    # print('total:',total, '\nremainder:',remainder)

    result = total * a

    if(remainder != 0):
        result += s[:remainder].count('a')

    return result


test1 = ['abcacb', 10]
test2 = ['a', 1000000000000]

print('\ntest1: ',repeatedString(test1[0], test1[1]), '\nanswer',4)
print('\ntest2:',repeatedString(test2[0], test2[1]), '\nanswer',1000000000000)
