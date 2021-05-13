import sys
sys.setrecursionlimit(100)

input = sys.stdin.readline

n, m = map(int,input().split())

li = []

for _ in range(n) :
    li.append(list(map(int,input().split())))

ali = [[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,1],[0,1]]
bli = [[0,2],[0,2],[0,2],[0,2],[0,2],[0,2],[0,2],[1,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[2,0],[1,1],[1,-1],[1,1],[1,0]]
cli = [[0,3],[1,2],[1,1],[1,0],[-1,0],[-1,1],[-1,2],[1,1],[0,1],[1,1],[2,1],[2,-1],[1,-1],[0,-1],[3,0],[2,1],[2,-1],[1,2],[1,-1]]

ans = 0
def fun(x, y) :
    for _ in range(19) :
        global ans
        p1 = [x+ali[_][0],y+ali[_][1]]
        p2 = [x+bli[_][0],y+bli[_][1]]
        p3 = [x+cli[_][0],y+cli[_][1]]

        if p1[0] < 0 or p2[0] < 0 or p3[0] < 0 or p1[0] >= n or p2[0] >= n or p3[0] >= n or p1[1] < 0 or p2[1] < 0 or p3[1] < 0 or p1[1] >= m or p2[1] >= m or p3[1] >= m :
            continue
        
        tmp = li[x][y]+li[p1[0]][p1[1]]+li[p2[0]][p2[1]]+li[p3[0]][p3[1]]
        if ans <= tmp :
            ans = tmp
        

for i in range(n) :
    for j in range(m) :
        fun(i, j)

print(ans)
    