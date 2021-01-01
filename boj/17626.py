import sys

input = sys.stdin.readline

n = int(input())
count = 0
li = [0] * (n+1)
li[1] = 1

for _ in range(2, n+1) :
    ans_count = 10e7
    tmp = int(_ ** 0.5)
    for i in range(tmp, tmp//2, -1) :
        x = _ - i ** 2
        count = li[x] + 1
        #print(i)
        ans_count = min(ans_count, count)
    li[_] = ans_count

print(li[n])

## 시간초과 해결하는 법 ? -- 3중 for 문으로 해결하는 법 공부하기
## li의 값이 5를 넘을 수 없음 왜 ? -- 증명 확인 할 것