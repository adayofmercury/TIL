#####

# 파이썬의 힙은 최소 힙밖에 구현이 안되기 때문에
# 최소 힙 최대 힙을 다 만들고 나서 튜플로 인덱스 저장
# visited 를 만들고 visited[index] 의 True False 여부로 힙에 있는지 없는지 확인
# visited[index] = false 이면 힙에서 빼는 과정 -> 다 빼고 나면 최대 최소는 맨 끝값일 것이므로 이를 확인 // 하나라도 비어있다면 빈 큐이므로 EMPTY 출력


import sys
import heapq

input = sys.stdin.readline


t = int(input())

for _ in range(t) :
    
    visited = []
    maxheap = []
    minheap = []
    index = 0

    k = int(input())
    for i in range(k) :
        command = input().split()
        if command[0] == 'I' :
            heapq.heappush(maxheap,(-int(command[1]),index))
            heapq.heappush(minheap,(int(command[1]),index))
            visited.append(True)
            index += 1

        elif command[0] == 'D' :
            if maxheap and minheap :
                wh = 0
                if int(command[1]) == 1 :
                    while minheap and not visited[maxheap[0][1]] : 
                        heapq.heappop(maxheap)
                    if maxheap :
                        v = heapq.heappop(maxheap)
                        visited[v[1]] = False
                elif int(command[1]) == -1 :
                    while minheap and not visited[minheap[0][1]] : 
                        heapq.heappop(minheap)
                    if minheap :
                        v = heapq.heappop(minheap)
                        visited[v[1]] = False
        
        #print(maxheap, minheap)
    
    while minheap and not visited[minheap[0][1]] : 
        heapq.heappop(minheap)
    while maxheap and not visited[maxheap[0][1]] : 
        heapq.heappop(maxheap)

    #print(maxheap, minheap)
    if maxheap and minheap :
        print(-maxheap[0][0],minheap[0][0])
    else :
        print('EMPTY')