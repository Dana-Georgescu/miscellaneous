#! /bin/python3
'''Challenge :
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen'''




def jumpingOnClouds():
    number_of_clouds = int(input())
    clouds = list(map(int, input().rstrip().split()))
    clouds.append(3)
    clouds.append(4)
    moves = 0
    current_cloud = 0
    while current_cloud < number_of_clouds-1:
        if clouds[current_cloud+2] == 0:
            current_cloud +=2
            moves +=1
        else:
            current_cloud +=1
            moves +=1
    return moves

print(jumpingOnClouds())
