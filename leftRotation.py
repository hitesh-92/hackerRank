import os
os.system('cls' if os.name == 'nt' else 'clear')
# nodemon --exec python3 test.py


def rotLeft(a, d):
    # for i in range(d): a = a[1:] + a[:1]
    # return a

    mod = d % len(a)
    # print(mod)

    a = a[mod:] + a[:mod]

    # for i in range(mod):
    #     a = a[1:] + a[:1]
    #     print(a)

    return a


print('\n--1-\n', rotLeft([1, 2, 3, 4, 5], 4) == [5,1,2,3,4] )
print('')

print('\n--2-\n', rotLeft(
[41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
, 10) ==
[77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77]
)
print('')
