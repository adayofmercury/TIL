a, b = map(int, input().split())

gy = 1
gb = 1

def gyb(a,b) :
    global gy, gb
    for i in range(2, min(a,b)+1) :
        if a % i == 0 and b % i == 0 :
            gy *= i
            a //= i
            b //= i
            return gyb(a,b)
    return print(gy, gy*a*b, sep='\n')
    
gyb(a,b)