from itertools import combinations
import sys

input = sys.stdin.readline

n, k = map(int,input().split())
itemli = []
maxvalue = -1
for _ in range(n) :
    w, v = map(int,input().split())
    itemli.append([w, v])

dp = [[0 for _ in range(k + 1)] for i in range(n + 1)]
#print(dp)
for i in range(1, n + 1) :
    v = itemli[i-1]
    for j in range(1, k + 1) :
        if j < v[0] :
            dp[i][j] = dp[i-1][j]
        if j >= v[0] :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[0]]+v[1])

#print(dp)
print(dp[n][k])