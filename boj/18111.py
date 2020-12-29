import sys
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int,input().split())

ground = []
for i in range(n) : # 땅 높이 입력받기
    ground += map(int,input().split())

ground = dict(Counter(ground)) # 시간초과를 피하기 위해서 같은 높이의 땅 좌표는 하나로 묶는다 -> 하나씩 확인하는 것 보다 시간절약가능
mx = max(ground.keys())
mn = min(ground.keys())

ans_time = 100000000000000
ans_height = -1


for x in range(mn, mx+1) :
    time = 0
    inven = b
    for key,value in ground.items() :
        if x < key :
            time += 2 * (key - x) * value
            inven += (key - x) * value
        elif key < x :
            time += 1 * (x - key) * value
            inven -= (x - key) * value
    if inven < 0 : # 인벤토리가 음의 값이면 시간 무시
        continue
    
    if time < ans_time : # 계산한 시간이 기존 값보다 작은지 확인
        ans_time = time
        ans_height = x
    elif time == ans_time : # 가장 높은 위치를 검색
        ans_height = max(ans_height,x)
                
print(ans_time, ans_height)


###
#collections counter / defaultdict를 이용해서 같은 높이의 블록은 하나로 묶어서 처리 -> 시간복잡도 해결
#다른 논리로 cpp로 풀면 시간복잡도 문제 없는데 파이썬이라 문제생기는 것
#
###