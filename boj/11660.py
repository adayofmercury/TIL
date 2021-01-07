import sys

input = sys.stdin.readline

n, m = map(int,input().split())

temp = []
li = [[10e7 for _ in range(n+1)] for a in range(n+1)]

for i in range(1, n+1) :
    temp = list((map(int,input().split())))
    li[i][0] = 0
    #print(temp)
    for j in range(1, n) :
        li[i][j+1] = li[i][j]+temp[j]

#print(li)

for m in range(m) :
    x1, y1, x2, y2 = map(int,input().split())
    sum = 0
    for x in range(x1, x2+1) :
        sum += li[x][y2] - li[x][y1-1]
    print(sum)

### 210105 벼락치기로 대충 풀기만하니까 복습을 안하는것같아서 class 4 부터는 하루동안 풀었던 문제를 간단히 정리해보겠습니다.

# 행으로 접근하는거까지는 좋았는데 누적합을 생각안했다
# 누적합으로 풀어도 시간초과뜨는데 ?
## DP + 누적합 문제라고 ??

## 누적합을 행으로 풀어서 python3 으로 풀면 시간초과가 나고 pypy로 하면 맞았습니다가 된거였음
## 누적합을 0,0 부터 x,y 까지의 합으로 구했다면 시간초과가 python3 에서도 나지 않았을 것.. 연습을 더 하자.. 보자마자 떠올릴 수 있게