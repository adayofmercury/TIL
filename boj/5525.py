n = int(input())
m = int(input())
s = input()

pn = 'IO' * n + 'I'

i = 0
ans = 0
count = 0

while i + len(pn) < m :
    #print(i)
    if s[i] == 'O' :
        i += 1
        continue
    elif s[i] == 'I' :
        i += 1
        while s[i:i+2] == 'OI' :
            count += 1
            i += 2
        if count >= n :
            ans += count - n + 1
        count = 0

""" while i+len(pn) < m :
    if s[i] == 'I' :
        if s[i:i+len(pn)] == pn :
            ans += 1
            i += 2
        else :
            i += 1
    elif s[i] == 'O' :
        i += 1
        continue
 """

print(ans)

## 슬라이싱이 string 범위를 넘어가도 왜 참조가 되는걸까 ?