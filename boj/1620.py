# 나는야 포켓몬 마스터 이다솜
# 문제가 길다


import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int,input().split())

dogam = defaultdict(str)

for _ in range(n) :
    name = input().rstrip()
    dogam[str(_+1)] = name
    dogam[name] = _+1

#print(dogam)

for _ in range(m) :
    put = input().rstrip()
    print(dogam[put])


# 나는 야매로 이렇게 풀었지만 다른 사람들 코드를 보니까 딕셔너리를 두개 만들거나 keys() 를 이용해서 이름들 리스트를 만들어 놓는 듯