import sys

input = sys.stdin.readline

A, P = map(int,input().split())

li = [A]

def fun(a) :
    tmp = str(a)
    tmpsum = 0

    for i in tmp :
        tmpsum += int(i) ** P

    if tmpsum in li :
        return print(li.index(tmpsum))
    else :
        li.append(tmpsum)
        fun(tmpsum)

fun(A)
