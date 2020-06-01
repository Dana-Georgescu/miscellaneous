#! usr/bin/python3.7

"Challenge https://www.hackerrank.com/challenges/birthday-cake-candles/problem"


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles():
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    return ar.count(max(ar))



print(birthdayCakeCandles())
