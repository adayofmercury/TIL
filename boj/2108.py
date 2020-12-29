import sys

input = sys.stdin.readline

n = int(input())
li = []

for i in range(n) :
    li.append(int(input()))


sum = 0
for i in li :
    sum += i

print(round(sum/n))


#중간값 -> 값이 여러개여도 적용하는 줄 몰랐지 ..

liset = set(li)
liset = list(liset)
liset.sort()
li.sort()
print(li[len(li)//2])


#최빈값
lidic = {}
for i in li :
    if i in lidic :
        lidic[i] += 1
    else :
        lidic[i] = 1

limax = []
for a, b in zip(list(lidic.keys()),list(lidic.values())) :
    if b == max(lidic.values()) :
        limax.append([a, b])
    

limax.sort(key = lambda x : (-x[1], x[0]))

if len(limax) >= 2 :
    print(limax[1][0])
else :
    print(limax[0][0])

#범위
li.sort()
print(li[-1] - li[0])
