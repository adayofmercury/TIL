import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
li = deque([])

for _ in range(n) :
    li.append(_+1)

while len(li)!=1 :
    li.popleft()
    #print(li)
    v = li.popleft()
    li.append(v)
    #print(li)

print(li[0])