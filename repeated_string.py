#! /bin/python3.7

'''Challenge https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen'''
#!/bin/python3


def repeatedString():
    string = 'a' #input()
    a_in_string = string.count('a')
    lenght = len(string) # is 3
    index = 1000000000000 #int(input())
    if index == lenght:
        return a_in_string
    elif index < lenght:
        return string[:index].count('a')
    else:
        cât = index // lenght
        rest = index % lenght
        a_cât = a_in_string * cât
        a_rest = string[:rest].count('a')
        return a_cât + a_rest
    


print(repeatedString())
