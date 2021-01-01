import sys

input = sys.stdin.readline

n = int(input())

li = [0] * (n+10)

li[1] = 1
li[2] = 2

if n > 2 :
    for i in range(3, n+1) :
        li[i] = li[i-2] + li[i-1]

print(li[n]%10007)
