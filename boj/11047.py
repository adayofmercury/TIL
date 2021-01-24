import sys
import heapq

input = sys.stdin.readline

n, k = map(int,input().split())
li = []
ans = 0

for _ in range(n) :
    heapq.heappush(li,-(int(input())))

while k != 0 :
    v = heapq.heappop(li)
    if (-v) <= k :
        tmp = k // (-v)
        k += v * tmp
        ans += tmp
print(ans)