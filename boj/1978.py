n = int(input())
li = list(map(int,input().split()))

count = 0

for i in li :
    if i == 1 :
        continue
    so = True
    for x in range(2,i) :
        if i % x == 0 :
            so = False
            break
    if so == True :
        count += 1

print(count)