import sys
import heapq

input = sys.stdin.readline

li = []

for _ in range(int(input())) :
    command = int(input())
    
    if command == 0 :
        if li :
            a = heapq.heappop(li)
            print(-a)
        else :
            print(0)
    else :
        heapq.heappush(li, -command)


# heapq는 최소힙이다, 파이썬은 최대 힙을 지원하지 않기 때문에 부호를 반대로 하는 등의 트릭을 통해 최대 힙을 구현해야