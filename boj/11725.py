import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

c = int(input())
tree = defaultdict(list)
li = deque([])
root = [0] * (c + 1)
visited = [False] * (c + 1)

for _ in range(c-1) :
    n, m = map(int,input().split())
    tree[n].append(m)
    tree[m].append(n)


def dfs(index) :
    li.append(index)
    visited[index] = True
    if li :
        v = li.pop()
    ##print(v)
        for _ in tree[v] :
            if visited[_] == False :
                dfs(_)
                root[_] = v


dfs(1)
for i in range(2,len(root)) :
    print(root[i])