import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
DP = [[10e7 for i in range(n+1)] for j in range(n+1)]

for _ in range(m) :
    x, y, z = map(int,input().split())
    DP[x][y] = min(DP[x][y], z)

#print(DP)

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if i == j : DP[i][j] = 0
            DP[i][j] = min(DP[i][j], DP[i][k]+DP[k][j])

for i in range(1, n+1) :
    for j in range(1, n+1) :
        print(DP[i][j] if DP[i][j] != 10e7 else 0, end=' ')
    print()
