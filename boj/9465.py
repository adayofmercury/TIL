import sys

input = sys.stdin.readline

for t in range(int(input())) :
    n = int(input())
    li = []
    for _ in range(2) :
        li.append(list(map(int,input().split())))   

    if n == 1 :
        max(li[0][0], li[0][1])
    elif n == 2 :
        max(li[0][0]+li[1][1], li[1][0]+li[0][1])
    else :
        li[0][1] += li[1][0]
        li[1][1] += li[0][0]
        for i in range(2,n) :
            for j in range(2) :
                if j == 0 :
                    li[j][i] = max(li[j][i]+li[1][i-1],li[j][i]+li[1][i-2])
                elif j == 1 :
                    li[j][i] = max(li[j][i]+li[0][i-1],li[j][i]+li[0][i-2])
    #print(li)
    print(max(li[0][-1],li[0][-2],li[1][-1],li[0][-2]))