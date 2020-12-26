import sys

input = sys.stdin.readline

n = (int)(input())
user = []
for _ in range(n) :
    a, b = input().split()
    user.append((a,b))


#user.sort(key = lambda x : (int(x[0])))

def age(x) :
    return int(x[0])

user.sort(key = age)

for a, b in user :
    print(a,b)



### .sort(key = lambda x : (int(x[0])))


#user.sort(key = lambda x : (int(x[0])))

#def age(x) :
#    return int(x[0])

# lambda x : 리턴 이니까 그냥 함수의 이름을 없앤다고 생각하면 될 듯 !