arr = [1, 2, 3, 4, 5]

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max_arr = arr.copy()
    min_arr = arr.copy()
    max_arr.remove(min(max_arr))
    min_arr.remove(max(min_arr))
    print(sum(min_arr) , sum(max_arr))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
