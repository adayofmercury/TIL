import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())


li = [10e7] * 100001
visited = [False] * 100001
q = deque([n])

def bfs(n) :
    if 2*n <= 100000 and visited[2 * n] == False :
        q.append(2*n)
        li[2 * n] = li[n] + 1
        visited[2 * n] = True
    if n-1 >= 0 and visited[n-1] == False:
        q.append(n-1)
        li[n-1] = li[n] + 1
        visited[n-1] = True
    if n+1 <= 100000 and visited[n+1] == False:
        q.append(n+1)
        li[n+1] = li[n] + 1
        visited[n+1] = True



li[n] = 0
visited[n] = True
while visited[k] == False :
    v = q.popleft()
    bfs(v)

print(li[k])


### 당연히 DP 문제인 줄 알고 쓰다가 보니까 아무리 모르겠어서 알고리즘 분류를 보고나서 겨우 BFS로 풀어야 한다는 것을 확인..
### 양치기 하다보면 해결될 문제인가 ? BFS 라는 사실을 알고 나니까 몇가지 특이케이스(k=n 이라던지,, 계산하다가 100000이 넘는 경우라던지,, )만 예외로 처리한 다음 해결할 수 있었음.