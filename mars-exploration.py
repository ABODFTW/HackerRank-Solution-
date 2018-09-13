import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    miss_trans = 0
    counter = 0
    for i in s:
        sos = s[counter:counter+3]
        char_index = 0
        for char in sos:
            # miss_transmeted = [1 if x == ""]
            if char_index == 0 and char != "S":
                miss_trans+=1
            if char_index == 1 and char != "O":
                miss_trans+=1
            if char_index == 2 and char != "S":
                miss_trans+=1
            char_index+=1
        counter+=3
        if counter == len(s):
            break
    return miss_trans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
