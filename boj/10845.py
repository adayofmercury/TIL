import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n) :
    command = input().rstrip()

    if command == 'back' :
        if queue :
            print(queue[-1])
        else :
            print(-1)
    elif command == 'front' :
        if queue :
            print(queue[0])
        else :
            print(-1)
    elif command == 'size' :
        print(len(queue))
    elif command == 'empty' :
        if queue :
            print(0)
        else :
            print(1)
    elif command == 'pop' :
        if queue :
            v = queue.popleft()
            print(v)
        else :
            print(-1)
    elif command[0:4] == 'push' :
        command, x = command.split(' ')
        queue.append(int(x))