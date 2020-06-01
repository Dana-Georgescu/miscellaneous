#! /bin/python3.7

'Challenge https://www.hackerrank.com/challenges/staircase/problem'


# Complete the staircase function below.
def staircase():
    n = int(input())
    string = ""
    for i in range(n):
        string += " " * (n-1) + "#" * (i+1) + "\n"
        n -= 1
    return string[:-1]     
        

    

print(staircase())

