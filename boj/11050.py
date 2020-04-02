import sys

def factorial(a) :
    ans = 1
    for _ in range(1,a+1) :
        ans *= _
    return ans

def main() :
    n , r = map(int,sys.stdin.readline().split())
    print(int(factorial(n) / (factorial(r)*factorial(n-r))))

main()
