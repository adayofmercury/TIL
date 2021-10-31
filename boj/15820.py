# 15820_B3_맞왜틀

import sys

input = sys.stdin.readline

s1, s2 = map(int,input().split())

compare = []
for i in range(s1+s2) :
    a, b = map(int, input().split())
    compare.append([a,b])
cnt = 0
for i in range(s1) :
    
    if compare[cnt][0] != compare[cnt][1] :
        print("Wrong Answer")
        exit()
    cnt+=1

for i in range(s2) :
    if compare[cnt][0] != compare[cnt][1] :
        print("Why Wrong!!!")
        exit()
    cnt+=1

print("Accepted")