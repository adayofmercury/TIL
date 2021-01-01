import sys
input = sys.stdin.readline


li = list(map(int,input().split()))

li.sort()

for i in li :
    print(i, end=' ')