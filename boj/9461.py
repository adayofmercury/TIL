import sys

input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    li = [0] * 101

    li[1], li[2], li[3] = 1, 1, 1
    li[4], li[5] = 2, 2
    
    if n > 5 :
        for i in range(6, n+1) :
            li[i] = li[i-1] + li[i-5]

    print(li[n])

# 5번까지는 각자 지정, 6번부터는 DP