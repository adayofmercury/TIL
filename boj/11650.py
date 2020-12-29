import sys

input = sys.stdin.readline

n = int(input())
v = []

for _ in range(n) :
    v.append(tuple(map(int,input().split())))

v.sort(key = lambda x : (x[1], x[0]))

######################################
#line 11 ==
#def xy(x):
#    return (x[0], x[1])

#v.sort(key= xy)
######################################

for a, b in v :
    print(a,b)


## line 8 에서 그냥 a,b 지정안하고 바로 v에 append 하기
## sort 에서 lambda 를 key로 쓰는법, lambda를 쓰지 않고 되는 법 까지 이해하기 !!!!