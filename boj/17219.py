import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int,input().split())

li = defaultdict(str)

for _ in range(n) :
    site, pw = input().split()
    li[site] = pw

for _ in range(m) :
    find = input().strip()
    print(li[find])

###
#input은 sys.stdin.readline 으로
#.strip() 은 string 받을 때 엔터 무시
#defaultdict 선언은 기본값 정해줘야하고, 키값으로 밸류에 접근할 수 있음
###