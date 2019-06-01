import os
os.system('cls' if os.name == 'nt' else 'clear')
# nodemon --exec python3 test.py


def rotLeft(a, d):
    for i in range(d): a = a[1:] + a[:1]
    return a


print('\n---\n', rotLeft([1, 2, 3, 4, 5], 4) )
