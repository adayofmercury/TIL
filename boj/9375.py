import sys
from itertools import combinations
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    dic = defaultdict(int)
    li = []
    sum = 1
    for i in range(n) :
        clo, ty = input().rstrip().split()
        dic[ty] += 1
    for x in dic.values() :
        li.append(x)
        
    for temp in li :
        sum *= temp + 1

    print(sum - 1)
                
