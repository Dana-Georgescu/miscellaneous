#! python3.7
'''Challenge https://www.hackerrank.com/challenges/mini-max-sum/problem'''


def miniMaxSum():
    arr = list(map(int, input().rstrip().split()))
    total = 0
    for i in range(5):
        total += arr[i]
    mini = total - max(arr)
    maxi = total - min(arr)
    return str(mini) + " " + str(maxi)



print(miniMaxSum())

