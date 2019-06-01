# import os
# os.system('cls' if os.name == 'nt' else 'clear')

def jumpingOnClouds(c):
    highest = len(c) - 1

    i = 0
    jumps = 0

    while(True):
        jump = i + 2
        if ( i == highest ): break
        elif ( jump <= highest and c[jump] != 1 ):
            jumps += 1
            i += 2
        else:
            jumps += 1
            i += 1

    return jumps;



test1 = [0, 0, 1, 0, 0, 1, 0]; #4
test2 = [0, 0, 0, 0, 1, 0]; #3
test3 = [0, 0, 0, 1, 0, 0]; #3
test4 = [0, 0, 0, 0, 0, 0, 0]; #4

# print(jumpingOnClouds(test1), 4)
# print(jumpingOnClouds(test2), 3)
# print(jumpingOnClouds(test3), 3)
# print(jumpingOnClouds(test4), 4)
# print('\nresult:', result);
