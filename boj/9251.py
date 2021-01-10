st = input()
st2 = input()

DP = [[0 for _ in range(len(st)+1)] for i in range(len(st2)+1)]


for x in range(1, len(st2)+1) :
    for y in range(1, len(st)+1) :
        #print(x, y)
        #print(DP)
        if st2[x-1] == st[y-1] :
            DP[x][y] = DP[x-1][y-1] + 1
        else :
            DP[x][y] = max(DP[x-1][y], DP[x][y-1])

print(DP[-1][-1])
