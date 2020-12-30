import sys
from collections import defaultdict

input = sys.stdin.readline

dbj = defaultdict(int)

n, m = map(int,input().split())

for _ in range(n+m) :
    dbj[input().rstrip()] += 1

ans = []
for key in dbj.keys() :
    if dbj[key] == 2 :
        ans.append(key)

ans.sort()
print(len(ans))
for _ in ans :
    print(_)