import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())

circle = deque([])
yo = []

for i in range(n) :
    circle.append(i)

while circle :
    for i in range(k-1) :
        v = circle.popleft()
        circle.append(v)
    b = circle.popleft()
    yo.append(b)

print('<',end='')
for _ in yo :
    if _ == yo[len(yo)-1] :
        print(_+1, end='')
    else : 
        print(_+1, end = ', ')
print('>')