import sys

input = sys.stdin.readline


for _ in range(int(input())) :
    n = int(input())
    li = [0] * (12)
    li[1] = 1
    li[2] = 2
    li[3] = 4

    if 3 < n :
        for i in range(4, n+1) :
            li[i] = li[i-1] + li[i-2] + li[i-3]
        print(li[i])
    else :
        print(li[n])
