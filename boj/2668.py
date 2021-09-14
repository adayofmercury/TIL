import sys

input = sys.stdin.readline

def dfs(i, tmpli1, tmpli2, visited) :
    global DP
    val1 = li1[i]
    val2 = li2[i]
    tmpli1.append(val1)
    tmpli2.append(val2)

    if visited[val2] == True :
        if set(tmpli1) == set(tmpli2) :
            for j in tmpli1 :
                DP[j] = True
    
    else :
        visited[val1] = True
        dfs(val2, tmpli1, tmpli2, visited)


N = int(input())
li1 = [ i for i in range(N+1) ]
li2 = [-9999]

DP = [False] * (N+1)

for _ in range(N) :
    i = int(input())
    li2.append(i)

for i in range(1, N+1) :
    if DP[i] == True : pass
    else :
        visited = [False] * (N+1)
        tmpli1 = []
        tmpli2 = []
        dfs(i, tmpli1, tmpli2, visited)

ans = [a for a in range(N+1) if DP[a] == True]
print(len(ans))
for i in ans :
    print(i)
