import sys

input = sys.stdin.readline

k, n = map(int,input().split())
li = []
for _ in range(k) :
    li.append(int(input()))


start = 1
end = max(li)

while start <= end :
    mid = (start + end) // 2
    count = 0
    
    for i in li :
        if i >= mid :
            count += i // mid
    
    if count < n :
        end = mid - 1
    else :
        result = mid
        start = mid + 1

print(result)

## comment
# i를 mid 로 나눌때 i가 더 큰지 확인 (떡볶이 떡 자르기 처럼 사실 나누는건 상관없지만 뺄때는 꼭 필요한 라인임)
# count 가 작으면 end 를 줄이고
# mid를 result 에 저장하는 것(최대값이니까)