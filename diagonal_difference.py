#!/bin/python3

''' Challenge from https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=internal-search'''



#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def diagonalDifference():
    arr = []
    diagonal1 = diagonal2 = 0
    n = int(input().strip())
    for s in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(n):
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][-(i+1)]
    return abs(diagonal1 - diagonal2)

print(diagonalDifference())
