import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

ava = []
available = [True] * 11

if m != 0 :
    li = list(map(int,input().split()))
    for i in li :
        available[i] = False

for i in range(0, 10) :
    if available[i] == True :
        ava.append(i)

ans = abs( 100 - n )

for i in range(0, 1000000) :
    tmp = True
    i_str = str(i)

    for j in i_str :
        if available[int(j)] == False :
            tmp = False
            break
    
    if tmp == True :
        ans = min(ans, abs(i - n) + len(str(i)))

print(ans)
    

