from bisect import bisect_left, bisect_right

def count_by_range(a, value) :
    r_index = bisect_right(a, value)
    l_index = bisect_left(a, value)
    return print(r_index - l_index, end = ' ')

    
n = int(input())
li = list(map(int,input().split()))

li.sort()

m = int(input())
k = list(map(int,input().split()))

for _ in k :
    count_by_range(li, _)

## line 3 - 6
## bisect_right (오른쪽에서 이진탐색해서 빈자리 인덱스 찾음)
## bisect_left (왼쪽에서 이진탐색해서 빈자리 인덱스 찾음)
## 오른 - 왼 하면 갯수가 몇갠지 나옴

## 딕셔너리 keys & value 를 이용해서 += 1 딕셔너리를 만들 수도 있음
## !!! ) 함수 / 딕셔너리 안 쓰고 이진탐색 손으로 구현하려면 lowerbound, upperbound 재귀로 구현해서 upper - lower ..
