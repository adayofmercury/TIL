import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
li = []
visited = [[False for i in range(n)] for _ in range(n)]
for _ in range(n) :
    tmp = input().rstrip()
    li.append(tmp)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, color) :
    for dli in range(4) :
        nx = x + dx[dli]
        ny = y + dy[dli]
            
        if nx >= n or nx < 0 or ny >= n or ny < 0 :
            continue
    
        if li[nx][ny] == color and visited[nx][ny] == False :
            visited[nx][ny] = True
            dfs(nx,ny,color)

def dfs_(x, y, color) :
    for dli in range(4) :
        nx = x + dx[dli]
        ny = y + dy[dli]
            
        if nx >= n or nx < 0 or ny >= n or ny < 0 :
            continue
    
        if li_[nx][ny] == color and visited[nx][ny] == False :
            visited[nx][ny] = True
            dfs_(nx,ny,color)


count = 0
for i in range(n) :
    for j in range(n) :
        if visited[i][j] == False :
            visited[i][j] = True
            count += 1
            dfs(i, j, li[i][j])

li_ = []
for i in range(n) :
    tmp = ''
    for j in range(n) :
        if li[i][j] == 'B' :
            tmp += 'B'
        else :
            tmp += 'G'

    li_.append(tmp)

visited = [[False for i in range(n)] for _ in range(n)]
count_ = 0
for i in range(n) :
    for j in range(n) :
        if visited[i][j] == False :
            visited[i][j] = True
            count_ += 1
            dfs_(i, j, li_[i][j])

# 적록색맹 R = B

print(count, count_)