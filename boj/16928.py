# 뱀과 사다리
import sys
from collections import deque

input = sys.stdin.readline

# 지도
board = []
visited = [False] * 110
for i in range(0,110) :
    board.append([i,i])

n, m = map(int,input().split())
for _ in range(n+m) :
    x, y = map(int,input().split())
    board[x][1] = y

#print(board)

li = deque([[1,0]])

def roll(cur) :
    for i in range(1,7) :
        temp = board[cur[0]+i][1]
        count = cur[1] + 1
        if visited[temp] == False :
            li.append([temp,count])
            visited[temp] = True
    #print(li)

while True :
    cur = li.popleft()
    if cur[0] == 100 :
        print(cur[1])
        break
    else :
        roll(cur)