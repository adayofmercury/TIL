import sys

input = sys.stdin.readline

n, m = map(int,input().split())

li = [[10e7 for _ in range(n+1)] for i in range(n+1)]

for i in range(m) :
    a, b = map(int,input().split())
    li[a][b] = 1
    li[b][a] = 1

for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            if a == b :
                li[a][b] = 0
            li[a][b] = min(li[a][b], li[a][k]+li[k][b])
            
val = 10e9
for a in range(1, n+1) :
    temp = 0
    for b in range(1, n+1) :
        temp += li[a][b]
    
    if val > temp :
        ans = a
        val = temp

    
print(ans)
    
# 플로이드 워셜