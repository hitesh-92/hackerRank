
# Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.


# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    result = int(0)
    for i in ar:
        result += int(i)
    return result


arr =[1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
aVeryBigSum(arr)