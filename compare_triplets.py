"Challenge  https://www.hackerrank.com/challenges/compare-the-triplets/problem"


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice +=1
        elif a[i] < b[i]:
            bob +=1     
    return str(alice) + " " + str(bob)
    
Alice = list(map(int, input().rstrip().split()))
Bob = list(map(int, input().rstrip().split()))

print(compareTriplets(Alice, Bob))
