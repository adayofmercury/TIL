n = int(input())
fac = 1
for i in range(1, n+1) :
    fac *= i

fac = str(fac)
count = 0
for i in range(len(fac), 0, -1) :
    if fac[i-1] == '0' :
        count += 1
    else :
        print(count)
        break