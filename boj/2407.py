n, m = map(int,input().split())
sumn, summ = 1, 1
for i in range(0, m) :
    sumn *= (n-i)
    summ *= (m-i)


print(sumn/summ)