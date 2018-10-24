#!/bin/python3



#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    return sum(ar) #sum of elements of array or list





ar_count = int(input()) #length of array

ar = list(map(int, input().rstrip().split())) #inputting elements

result = simpleArraySum(ar)

print(result)