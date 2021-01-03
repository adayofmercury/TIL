import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int,input().split())

li = []

for _ in range(n) :
    li.append(list(map(int,input().split())))

#print(li)
q = deque([])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
ans = 1

for x in range(n) :
    for y in range(m) :
        if li[x][y] == 1 :
            q.append([x, y])
            #print(q)

def bfs(x, y) :
    global ans
    for i in range(4) :
        x_ = x + dx[i]
        y_ = y + dy[i]
        if x_ < n and x_ >= 0 and y_ < m and y_ >= 0 :
            if li[x_][y_] == 0 :
                li[x_][y_] = li[x][y] + 1
                q.append([x_, y_])
                ans = max(ans, li[x_][y_])
                #print(x_, y_, ans)

while q :
    a, b = q.popleft()
    bfs(a, b)

#print(li)

for x in range(n) :
    for y in range(m) :
        if li[x][y] == 0 :
            ans = 0
            #print(q)

print(ans-1)

## 1인 자리를 먼저 큐에 넣고 한번씩 실행시켜서 순서대로 실행시켜서 최대를 구할 수 있도록 함
## 표 문제라서 visited 배열을 만들 필요가 없이 표에다가 직접 입력하면서 진행함
