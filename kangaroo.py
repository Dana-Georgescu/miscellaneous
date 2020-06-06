#! usr/bin/python3.7
'''Challenge https://www.hackerrank.com/challenges/kangaroo/problem'''



def kangaroo():
    OllieJane = input().split()
    print(OllieJane)
    positionOllie = int(OllieJane[0])
    leapOllie = int(OllieJane[1])
    positionJane = int(OllieJane[2])
    leapJane = int(OllieJane[3])
    #print(positionOllie, leapOllie, positionJane, leapJane)
    if positionOllie > positionJane:
        positionOllie, leapOllie, positionJane, leapJane = positionJane, leapJane, positionOllie, leapOllie
    print(positionOllie, leapOllie, positionJane, leapJane)
    if leapOllie <= leapJane:
        return "NO"
    while positionOllie <= positionJane:
        positionOllie += leapOllie
        positionJane += leapJane
        print(positionOllie, positionJane)
        if positionOllie == positionJane:
            return "YES"
    return "NO"
        
        
    
    


print(kangaroo())

