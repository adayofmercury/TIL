import sys
from collections import deque
import heapq

input = sys.stdin.readline

n, e = map(int,input().split())
distance = [10e7] * (n+1)
q = []

k = int(input())

li = [[] for i in range(n+1)]

for _ in range(e) :
    u, v, w = map(int,input().split())
    li[u].append((v,w))

#print(li)

### 다익스트라 구현

def dijkstra(start) :
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        
        for i in li[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(k)

for i in distance[1:] :
    print(i if i != 10e7 else 'INF')
