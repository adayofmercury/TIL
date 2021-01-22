n = int(input())
li = [0] * n

li[0] = 1
if n > 1 :
    li[1] = 3

if n > 2 :
    for i in range(2, n) :
        li[i] = li[i-1] + li[i-2] * 2

print(li[n-1]%10007)

#DP