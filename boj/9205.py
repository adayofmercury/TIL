import sys
from collections import deque

input = sys.stdin.readline


for testcase in range(int(input())) :
    q = []
    n = int(input())

    for pyun in range(n+2) :
        px, py = map(int,input().split())
        q.append((px,py))

    v = [[10e7 for i in range(n+2)] for _ in range(n+2)]

    for i in range(n+2) :
        for j in range(n+2) :
            if i == j :
                continue
            distance = abs(q[i][0] - q[j][0]) + abs(q[i][1] - q[j][1])
            if distance <= 1000 :
                v[i][j] = 1
    
    for k in range(n+2) :
        for i in range(n+2) :
            for j in range(n+2) :
                if (v[i][j] > v[i][k] + v[k][j]) :
                    v[i][j] = v[i][k] + v[k][j]

    if v[0][-1] == 10e7 :
        print('sad')
    else :
        print('happy')
   