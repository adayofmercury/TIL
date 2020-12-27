import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

li.sort()

m = int(input())

k = list(map(int,input().split()))

for _ in k :
    start = 0
    end = n-1
    have = 0
    while start <= end :
        mid = (start+end) // 2
        if li[mid] == _ :
            have = 1
            break
        else :
            if li[mid] < _ :
                start = mid + 1
            else :
                end = mid - 1

    print(have)


## pypy 로 풀면 
####
#import sys
#input = sys.stdin.readline

#n = int(input())

#li = list(map(int,input().split()))

#m = int(input())

#k = list(map(int,input().split()))

#for _ in k :
#    if _ in li :
#        print(1)
#    else :
#        print(0) 

### 도 정답 처리가 되는데, python에서는 시간초과가 됨
### 이진검색을 사용해서 시간초과 막기
####