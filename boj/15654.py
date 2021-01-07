n, m = map(int,input().split())
sortedli = list(map(int,input().split()))
sortedli.sort()
visited = [False] * len(sortedli)
ans = []

def dfs(index) :
    for i in range(0, len(sortedli)) :
        if visited[i] == True :
            continue

        elif visited [i] == False :
            visited[i] = True
            ans.append(sortedli[i])
            if len(ans) == m :
                print(*ans)
            else :
                dfs(index)
            
            visited[i] = False
            ans.pop()

dfs(0)