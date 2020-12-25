import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m) :
    c, vertex = map(int, sys.stdin.readline().rstrip().split())
    graph[c].append(vertex)

# 최단 거리니까 bfs를 써보자

queue = deque([x])
visited = [-1] * (n+1) 
#print(queue)

while queue :
    v = queue.popleft()
    for i in graph[v] :
        if visited[i] == -1 :
            visited[i] = visited[v] + 1
            queue.append(i)
    #print(v)
    #print(visited)
visited[x] = -1
for i in range(len(visited)) :
    if visited[i] == k-1 :
        print(i)
if not k-1 in visited :
    print(-1)


    ##### check point

    # input() 보다 sys.stdin.readline().rstrip() 을 통해서 해결할 것
    # import sys 해야함

    ###

    # 최단거리문제에서 시작 노드로 돌아오는 것을 해결하기 위해 예외처리를 할것 (line 25)
    # 리스트 컴프리헨션으로 2차원 배열을 만들것(deep copy 방지) (line 5)