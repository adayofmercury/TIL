import sys

input = sys.stdin.readline

n, m = map(int, input().split())

li = list(map(int,input().split()))

#print(li)

for i in range(1, n) :
    li[i] += li[i-1]

#print(li)

for _ in range(m) :
    x, y = map(int, input().split())
    if x == 1 :
        print(li[y-1])
    else :
        print(li[y-1]-li[x-2])