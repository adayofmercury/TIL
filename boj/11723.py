import sys

input = sys.stdin.readline
s = set()
onetwenty = set([str(i) for i in range(1,21)])
for _ in range(int(input())) :
    command = input().rstrip().split()
    if command[0] == 'add' :
        s.add(command[1])
    elif command[0] == 'remove' :
        try : s.remove(command[1])
        except : pass
    elif command[0] == 'check' :
        if command[1] in s :
            print(1)
        else :
            print(0)
    elif command[0] == 'toggle' :
        if command[1] in s :
            s.remove(command[1])
        else :
            s.add(command[1])
    elif command[0] == 'all' :
        s = onetwenty
    elif command[0] == 'empty' :
        s = set()

## remove 는 없으면 런타임 에러가 나니까 try except 문으로 처리할 것
## rstrip().split() 으로 나누면 리스트 안에 두개로 나눌 수 있다 !