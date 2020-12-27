import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n) :
    command = input().rstrip()

    if command == 'top' :
        if stack :
            print(stack[-1])
        else :
            print(-1)
    elif command == 'size' :
        print(len(stack))
    elif command == 'empty' :
        if stack :
            print(0)
        else :
            print(1)
    elif command == 'pop' :
        if stack :
            v = stack.pop()
            print(v)
        else :
            print(-1)
    elif command[0:4] == 'push' :
        command, x = command.split(' ')
        stack.append(int(x))