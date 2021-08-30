import sys

input = sys.stdin.readline

n = int(input())

li_t = []
li_p = []

for i in range(n) :
    tmp_t, tmp_p = map(int,input().split())

    li_t.append(tmp_t)
    li_p.append(tmp_p)
    
DP = [0] * (n+1)
    
for i in range(n-1, -1, -1) :
    if i + li_t[i] <= n :
        DP[i] = max(DP[i+1], li_p[i] + DP[i+li_t[i]])
    else :
        DP[i] = DP[i+1]
print(DP[0])
        
