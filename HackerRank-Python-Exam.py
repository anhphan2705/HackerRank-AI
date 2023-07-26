

#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    grid = np.array(grid)
    padded = np.pad(grid, (1,), constant_values=0)
    kernel = []
    maxs = []
    for h in range(len(grid)):
        for w in range(len(grid[0])):
            kernel = padded[h:h+3, w:w+3]
            kernel = list(kernel.flatten())
            max_val = max(kernel)
            if max_val == grid[h][w] and kernel.count(max_val) == 1:
                maxs.append(max_val)
    return len(maxs)

def missingCharacters(s):
    string = ''
    sort_str = sorted(set(list(s)))
    for index in range(48, 58):
        if chr(index) not in sort_str:
            string = string + chr(index)
    for index in range(97, 123):
        if chr(index) not in sort_str:
            string = string + chr(index)
    return string
    
if __name__ == '__main__':
    grid = [[0, -1, 7], [-2, -3,], [8, 8, 9]]
    sample = '8hypotheticall024y6wxz'
    # print(numCells(grid))
    # print(missingCharacters(sample))
    num = "f;f;f;"
    num= num.split(';')
    print(num)