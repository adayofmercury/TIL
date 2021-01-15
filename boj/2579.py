import sys

input = sys.stdin.readline
li = []
ans = 0 

for _ in range(int(input())) :
    li.append(int(input()))

DP = [0] * len(li)

if len(li) == 1 :
    print(li[0])
elif len(li) == 2 :
    print(li[0]+li[1])
else :
    for i in range(3, len(li)) :
        DP[0] = li[0]
        DP[1] = li[0]+li[1]
        DP[2] = max(li[0]+li[2], li[1]+li[2])
        DP[i] = max(DP[i-2]+li[i], DP[i-3]+li[i-1]+li[i])
    print(DP[-1])