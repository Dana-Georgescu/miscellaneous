#! usr/bin/python3.7

'''Challenge https://www.hackerrank.com/challenges/apple-and-orange/problem'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges():
    st = input().split()
    houseStart = int(st[0])
    houseEnd = int(st[1])
    ab = input().split()
    appleTree = int(ab[0])
    orangeTree = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    apples_house = oranges_house = 0
    
    for apple in apples:
        if (appleTree + apple) in range(houseStart, houseEnd + 1):
            apples_house += 1
    for orange in oranges:
        if (orangeTree + orange) in range(houseStart, houseEnd + 1):
            oranges_house += 1        
    return str(apples_house)+'\n'+str(oranges_house)

print(countApplesAndOranges())
