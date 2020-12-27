import sys

input = sys.stdin.readline

n = int(input())
li = []
rank= [] * n

for _ in range(n) :
    li.append(list(map(int,input().split())))
    li[_].append(_)
    li[_].append(1)

for i in range(n) :
    for j in range(n) :
        if li[i][1] < li[j][1] and li[i][0] < li[j][0]:
            li[i][3] += 1
    li[i].append(li[i][3])


for _ in range(n) :
    print(li[_][4], end = ' ')