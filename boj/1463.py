import sys

x = (int)(sys.stdin.readline().rstrip())

d = [0] * (10 ** 6 + 1)

for i in range(2, x+1) :
    d[i] = d[i-1] + 1
    if i % 2 == 0 :
        d[i] = min(d[i],d[i//2] + 1)
    if i % 3 == 0 :
        d[i] = min(d[i],d[i//3]  +1)

print(d[x])

## DP문제의 경우 점화식을 먼저 세우기 (bottom up)
## 이번문제의 경우 계산 카운트 = 이전의 것 + 1 이라는 생각을 했어야함
