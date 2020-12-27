import sys
input = sys.stdin.readline

n = int(input())
li = []
c = 0
while True :
    c += 1
    if '666' in str(c) :
        li.append(c)
        if len(li) == n :
            break

print(li[n-1])