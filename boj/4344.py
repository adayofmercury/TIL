import sys

input = sys.stdin.readline

for _ in range(int(input())) :
    count = 0
    li = list(map(int,input().split()))
    n = li[0]
    average = int(sum(li)/(len(li)-1))
    for i in li[1:] :
        if i >= average :
            count += 1
    #print(average)
    print(str(format(round(count/(len(li)-1)*100,3),".3f")) + "%")