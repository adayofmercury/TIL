import sys

input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n) :
    li.append(list(map(int,input().split())))

if n == 1 :
    print(min(li[0][0],li[0][1],li[0][2]))
elif n == 2 :
    for j in range(3) :
        li[1][j] = min(li[1][j] + li[0][j-1], li[1][j] + li[0][j-2])
    print(min(li[1][0]),li[1][1], li[1][2])
else :
    for i in range(1, n) :
        for j in range(3) :
            li[i][j] = min(li[i][j] + li[i-1][j-1], li[i][j] + li[i-1][j-2])
    print(li)
    print(min(li[n-1][0],li[n-1][1],li[n-1][2]))