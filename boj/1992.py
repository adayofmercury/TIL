import sys

input = sys.stdin.readline

n = int(input())
li = []

for i in range(n) :
    li.append(input())

def fun(x_, y_, temp) :
    
    for x in range(x_, x_ + temp) :
        for y in range(y_, y_ + temp) :
            #print('--', x,y, '--')
            if li[x_][y_] == li[x][y] :
                te = 1
            else :
                te = 0
                break
        if te == 0 :
            break
    if te == 0 :
        print('(', end='')
        fun(x_, y_, temp//2)
        fun(x_, y_ + temp//2, temp//2)
        fun(x_ + temp//2, y_, temp//2)
        fun(x_ + temp//2, y_ + temp//2, temp//2)
        print(')', end='')
    elif te == 1 :
        if li[x_][y_] == '1' :
            print(1, end='')
        else :
            print(0, end='')
    

fun(0, 0, n)

## 다를때 가르기 전에만 괄호 쳐주면 됩니다