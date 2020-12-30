import sys

input = sys.stdin.readline

n = int(input())


for i in range(n) :
    k = int(input())
    
    li = []
    li.append(list([1, 0]))
    li.append(list([0, 1]))
    for i in range(2, k+1) :
        li.append([li[i-1][0] + li[i-2][0], li[i-1][1] + li[i-2][1]])

    print(li[k][0], li[k][1])