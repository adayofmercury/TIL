n = int(input())

li = list(map(int,input().split()))

ans = [1 for i in range(n)]

for i in range(n) :
    for j in range(i) :
        if li[j] < li[i] :
            ans[i] = max(ans[i], ans[j]+1)

print(max(ans))

## 나보다 작은 것으로부터 +1 max값