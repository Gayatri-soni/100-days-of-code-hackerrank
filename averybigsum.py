# Sample Input
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005
# Output
# 5000000015



import math
import os
import random
import re
import sys


# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    return sum(ar)


ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)
print(result)
