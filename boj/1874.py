import sys
input = sys.stdin.readline

n = int(input())

ans = []
li = []

for _ in range(n) :
    ans.append(int(input()))
counter = 1

pr = []

for i in range(n) :
    while counter<=n+1 :
        if li == [] :
            pr.append('+')
            li.append(counter)
            counter += 1
        elif li[-1] == ans[i] :
            pr.append('-')
            li.pop()
            break
        else :
            pr.append('+')
            li.append(counter)
            counter += 1

if len(pr) != n*2 :
    print('NO')
else :
    for i in pr :
        print(i)

# while true 설정시 어디선가 무한루프를 돌았는지 메모리 오류가 계속났다. 웬만하면 while true는 피하자 확실한 조건값을 넣자..