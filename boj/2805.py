import sys

input = sys.stdin.readline

n, m = map(int,input().split())

tree = list(map(int,input().split()))

#print(tree)
start = 0
end = max(tree)

result = 0

while(start <= end) :
    total = 0
    mid = (start + end) // 2

    for _ in tree :
        if _ > mid :
            total += _ - mid
    
    if total < m :
        end = mid - 1
    else :
        result = mid
        start = mid + 1

print(result)

### 이분탐색 아이디어 -> 중간 + 1을 start로 바꾸거나 중간 - 1을 end로 바꿔서 반복문 돌리기
## python 으로 돌리면 시간 초과 오류가 발생하는데, pypy로 돌리면 괜찮음 (시간복잡도에 대한 이해가 필요)