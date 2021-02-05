import sys

input = sys.stdin.readline

li = []
n = int(input())
for _ in range(n) :
    li.append(list(map(int,input().split())))

for i in range(n) :
    for j in range(n) :
        if li[i][j] == 0 :
            li[i][j] = 10e7

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if li[i][k] + li[k][j] < li[i][j] :
                li[i][j] = li[i][k] + li[k][j]


for i in range(n) :
    for j in range(n) :
        if li[i][j] == 10e7 :
            li[i][j] = 0
        else :
            li[i][j] = 1

for i in range(n):
    for j in range(n) :
        print(li[i][j], end=' ')
    print()