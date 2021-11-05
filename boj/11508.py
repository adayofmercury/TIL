import sys

input = sys.stdin.readline

N = int(input())

li = []
for i in range(N) :
    li.append(int(input()))


li.sort(reverse=True)

ans = 0
for i in range(len(li)) :
    if (i+1) % 3 != 0 :
        ans += li[i]

print(ans)
