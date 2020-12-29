import sys

input = sys.stdin.readline


n = int(input())
li = list(map(int,input().split()))

li.sort()

m = int(input())
k = list(map(int,input().split()))

ans = []
for _ in k :
    start = 0
    end = n - 1
    count = 0
    while start != end :
        mid = (start+end) // 2
        if li[mid] == _ :
            count += 1
        if li[mid] < _ :
            start = mid + 1
        else :
            end = mid - 1
    
    ans.append(count)

for i in ans :
    print(i, end = '')
