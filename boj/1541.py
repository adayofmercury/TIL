sic = input()
temp = ''
li = []
li2 = []

for i in sic :
    if i != '+' and i != '-' :
        temp += i
    elif i == '-' :
        li.append(int(temp))
        li.append('-')
        temp = ''
    elif i == '+' :
        li.append(int(temp))
        li.append('+')
        temp = ''

li.append(int(temp))

li2.append(li[0])
for i in range(1, len(li)-1) :
    if li[i] == '+' :
        li2[-1] += li[i+1]
    elif li[i] == '-' :
        li2.append(li[i+1])

ans = li2[0]
for i in range(1, len(li2)) :
    ans -= li2[i]
print(ans)

## 덧셈을 먼저 많이함