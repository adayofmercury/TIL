import sys
input = sys.stdin.readline
li = []
white = 0
blue = 0

def sep(startx, starty, n) :
    global blue, white
    color = li[startx][starty]
    same = True
    for x in range(startx, startx+n) :
        for y in range(starty, starty+n) :
            if li[x][y] != color :
                same = False
                break
        if same == False :
            break
    
    if same == False :
        temp = int(n/2)
        sep(startx, starty + temp, temp)
        sep(startx + temp, starty, temp)
        sep(startx, starty, temp)
        sep(startx + temp, starty + temp, temp)
    
    if same == True :
        if color == 0 :
            white += 1
        elif color == 1 :
            blue += 1



n = int(input())
for _ in range(n) :
    li.append(list(map(int,input().split())))

sep(0, 0, n)

print(white)
print(blue)

## 파이썬 함수선언을 어디서해야되는지 잘 모르겠음 ㅡㅡ
## global 개념도 잘 모르겟고
## 아무튼 분할정복 !