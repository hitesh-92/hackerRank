import os
os.system('cls' if os.name == 'nt' else 'clear')
# nodemon --exec python3 test.py

def hourglassSum(arr):

    def add(one, two, three):
        result = 0
        print('add:: ',one, two, three)
        for i in one: result += i;
        print('res:  ',result)
        for i in two: result += i;
        print('res:  ',result)
        for i in three: result += i;
        print('res:  ',result)
        return result

    highest = float('-inf');

    for h in range(4):
        for v in range(4):

            top = arr[h][v:v+3]
            mid = arr[h+1][v+1:v+2]
            bot = arr[h+2][v:v+3]
            # print(top,mid,bot)
            total = add(top,mid,bot)
            # print(total)
            if total > highest:
                highest = total
            print('highest:',highest)
            print('total > highest:', total > highest)
            print('')
    return highest

test = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

test1 = [
    [0,-4,-6,0,-7,-6],
    [-1,-2,-6,-8,-3,-1],
    [-8,-4,-2,-8,-8,-6],
    [-3,-1,-2,-5,-7,-4],
    [-3,-5,-3,-6,-6,-6],
    [-3,-6,0,-8,-6,-7]
]

# print(hourglassSum(test));
print(hourglassSum(test1));
