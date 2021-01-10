a, b, c = map(int,input().split())

def fun(a, b) :
    if b == 1 :
        return a
    if (b % 2 > 0) :
        return fun(a, b-1) * a
    temp = fun(a, b//2) % c
    return temp ** 2 % c

print(fun(a, b) % c)