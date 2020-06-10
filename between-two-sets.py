#! usr/bin/python3.7

'''Challenge https://www.hackerrank.com/challenges/between-two-sets/problem'''
#!/bin/python3

# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def getTotalX():
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr1 = list(map(int, input().rstrip().split()))
    arr2 = list(map(int, input().rstrip().split()))
    arr1.sort()
    arr2.sort()
    interval = [x for x in range(max(arr1), min(arr2)+1)]
    multiples = []
    factors = []
    for a in interval:
        if list(filter(lambda x : a % x == 0, arr1)) == arr1:
            multiples.append(a)
    for m in multiples:
        if list(filter(lambda x : x % m == 0, arr2)) == arr2:
            factors.append(m)
    return(len(factors))        
    
print(getTotalX())
 
