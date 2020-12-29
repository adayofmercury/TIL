import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())) :
    li = deque([])
    n, m = map(int,input().split())

    li = deque(map(int,input().split()))
    ind = deque([])

    for i in range(n) :
        ind.append(i)

    cnt = 0
    while li :
        mx = max(li)
     
        if mx == li[0] :
            li.popleft()
            v = ind.popleft()
            #print(v)
            cnt += 1

            if v == m :
                print(cnt)
                break
        else :
            v = li.popleft()
            x = ind.popleft()
            li.append(v)
            ind.append(x)
        
        