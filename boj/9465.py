import sys

input = sys.stdin.readline

for T in range(int(input())) :

    sticker = []
    cols = int(input())
    for rows in range(2) :
        sticker.append(list(map(int,input().split())))

    for i in range(cols) :
        for j in range(2) :

            a,b,c = 0,0,0

            if j == 0:

                if i-2 >= 0: a = sticker[j][i-2] 
                if i-2 >= 0: b = sticker[1][i-2] 
                if i-1 >= 0: c = sticker[1][i-1]

                tmp = sticker[j][i]

                sticker[0][i] = max(tmp+a, tmp+b, tmp+c)

            elif j == 1:

                if i-2 >= 0: a = sticker[j][i-2]
                if i-2 >= 0: b = sticker[0][i-2]
                if i-1 >= 0: c = sticker[0][i-1]

                tmp = sticker[j][i]

                sticker[1][i] = max(tmp+a, tmp+b, tmp+c)

    print(max(sticker[0][cols - 1],sticker[1][cols - 1]))
