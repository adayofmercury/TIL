import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

li = list(map(int,input().split()))

li2 = li.copy()
dic = defaultdict(int)
li2.sort()
li3 = [0] * (n+1)
li3[0] = 0

for _ in range(n - 1) :
    if li2[_+1] == li2[_] :
        li3[_+1] = li3[_]
    else :
        li3[_+1] = li3[_] + 1

    dic[li2[_]] = li3[_]

dic[li2[n-1]] = li3[n-1]

for i in li :
    print(dic[i], end = ' ')