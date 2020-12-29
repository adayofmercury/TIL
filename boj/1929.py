#에라토네스의 체
#2가 소수면 4 6 8 10 12 ... 제거
#3이 소수면 6 8 9 12 ... 제거하는 방식
#소수구할때 앞으로 이렇게 (시간복잡도 감소)

m, n = map(int,input().split())
li = [True] * (n + 1)
li[1] = False
li[2] = True
for i in range(2, int((n ** 0.5)+1)) :
    
    if li[i] == True :
        count = 2
        while i * count < len(li) :
            li[i*count] = False
            count += 1
            

for i in range(m, n+1) :
    if li[i] == True :
        print(i)
