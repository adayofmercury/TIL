import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
li = []
count = 0
q = deque([])
visited = [[False for i in range(m)] for _ in range(n)]
#print(visited)

dxlist = [0,0,1,-1]
dylist = [1,-1,0,0]

for i in range(n) :
    li.append(list(map(int,list(input().strip()))))

def bfs(x, y, distance) :
    #print(x,y)
    q.append((x, y, distance))
    while q :
        #print(q)
        #print(li)
        x_, y_, dist = q.popleft()
        li[x_][y_] = dist
        for i in range(4) :
            dx = x_+dxlist[i]
            dy = y_+dylist[i]
            if dx < 0 or dy < 0 or dx >= n or dy >= m :
                continue
            else :
                if li[dx][dy] == 1 :
                    if visited[dx][dy] == False :
                        q.append((dx, dy, dist + 1))
                        visited[dx][dy] = True

        
bfs(0, 0, 1)

#print(li)
print(li[-1][-1])


####### BFS 다시 개념