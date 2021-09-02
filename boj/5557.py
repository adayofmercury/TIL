import sys

input = sys.stdin.readline

N = int(input())

li = list(map(int,input().split()))

DP = [ [0 for _ in range(21)] for i in range(N-1)]

DP[0][li[0]] = 1

for i in range(1, N-1) :
    for j in range(21) :

        if 0 <= j + li[i] <= 20 :
            DP[i][j] += DP[i-1][j+li[i]]
        if 0 <= j - li[i] <= 20 :
            DP[i][j] += DP[i-1][j-li[i]]

print(DP[-1][li[-1]])


        
