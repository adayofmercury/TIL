import sys

input = sys.stdin.readline

n = int(input())

li = [0] * 10001

for _ in range(n) :
    tmp = int(input())
    li[tmp] += 1

for i in range(10001) :
    if li[i] != 0 :
        for j in range(li[i]) :
            print(i)


### counting sort ? 수가 정해져있으면 이게 개빠르다고함