import sys
from collections import deque

input = sys.stdin.readline



for i in range(int(input())) :
    visited = [False] * 10001
    li = deque([])
    x, y = map(int,input().split())
    li.append([x,''])
    while True :
        temp = li.popleft()
        #print(temp)
        if temp[0] == y :
            print(temp[1])
            break
            
        # D 수행
        if temp[0] * 2 >= 10000 :
            newtemp = (temp[0] * 2) % 10000
        else :
            newtemp = temp[0] * 2
        
        if visited[newtemp] == False :
            visited[newtemp] = True
            li.append([newtemp,temp[1]+'D'])
        
        # S 수행
        if temp[0] == 0 :
            newtemp = 9999
        else :
            newtemp = temp[0] - 1
        
        if visited[newtemp] == False :
            visited[newtemp] = True
            li.append([newtemp,temp[1]+'S'])
        
        # L 수행
        tempstr = str(temp[0])
        len_temp = len(tempstr)
        if len_temp == 4 :
            newtemp = int(tempstr[1]+tempstr[2]+tempstr[3]+tempstr[0])
        elif len_temp == 3 :
            newtemp = int(tempstr[0]+tempstr[1]+tempstr[2]+'0')
        elif len_temp == 2 :
            newtemp = int('0'+tempstr[0]+tempstr[1]+'0')
        elif len_temp == 1 :
            newtemp = int('0'+'0'+tempstr[0]+'0')

        if visited[newtemp] == False :
            visited[newtemp] = True
            li.append([newtemp,temp[1]+'L'])
        
        # R 수행
        tempstr = str(temp[0])
        len_temp = len(tempstr)
        if len_temp == 4 :
            newtemp = int(tempstr[3]+tempstr[0]+tempstr[1]+tempstr[2])
        elif len_temp == 3 :
            newtemp = int(tempstr[2]+'0'+tempstr[0]+tempstr[1])
        elif len_temp == 2 :
            newtemp = int(tempstr[1]+'0'+'0'+tempstr[0])
        elif len_temp == 1 :
            newtemp = int(tempstr[0]+'0'+'0'+'0')

        if visited[newtemp] == False :
            visited[newtemp] = True
            li.append([newtemp,temp[1]+'R'])