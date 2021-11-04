import sys
input = sys.stdin.readline

TYPE = { 1 : [[0], [1], [2], [3]], 2 : [[0,2], [1,3]], 3:[[0,1], [1,2], [2,3], [0,3]], 4: [[0,1,2], [1,2,3], [2,3,0], [3,0,1]], 5:[[0,1,2,3]]}
CCTV_INFO = []

MAP = []
ans = 10e7

n, m = map(int,input().split())

for _ in range(n) :
    tmpM = list(map(int,input().split()))
    MAP.append(tmpM)
    for idx, tmp in enumerate(tmpM) :
        if tmp in [1,2,3,4,5] :
            CCTV_INFO.append([tmp, idx, _])

def mapControl(commands, targetMap, CCTV_X, CCTV_Y) :
    for command in commands :
        cnt = 1
        if command == 0 : #LEFT
            while CCTV_X - cnt >= 0 and targetMap[CCTV_Y][CCTV_X - cnt] != 6 :
                if targetMap[CCTV_Y][CCTV_X - cnt] == 0 :
                    targetMap[CCTV_Y][CCTV_X - cnt] = -1
                cnt += 1
        
        elif command == 1 : #UP
            while CCTV_Y - cnt >= 0 and targetMap[CCTV_Y-cnt][CCTV_X] != 6 :
                if targetMap[CCTV_Y-cnt][CCTV_X] == 0 :
                    targetMap[CCTV_Y-cnt][CCTV_X] = -1
                cnt += 1    

        elif command == 2 : #RIGHT
            while CCTV_X + cnt < m and targetMap[CCTV_Y][CCTV_X + cnt] != 6 :
                if targetMap[CCTV_Y][CCTV_X + cnt] == 0 :
                    targetMap[CCTV_Y][CCTV_X + cnt] = -1
                cnt += 1    

        elif command == 3 : #DOWN
            while CCTV_Y + cnt < n and targetMap[CCTV_Y + cnt][CCTV_X] != 6 :
                if targetMap[CCTV_Y + cnt][CCTV_X] == 0 :
                    targetMap[CCTV_Y + cnt][CCTV_X] = -1
                cnt += 1
    '''
    for line in targetMap :
        print(line)
    print('*******')
    '''

def getMin(MAP) :
    global ans
    tmpMin = 0
    for line in MAP :
        tmpMin += line.count(0)
    if ans > tmpMin :
        ans = tmpMin

def dfs(depth, MAP) :
    if depth == len(CCTV_INFO) :
        getMin(MAP)
        return
    for i in TYPE[CCTV_INFO[depth][0]] :
        tmpMAP = deepCopy(MAP)
        mapControl(i, MAP, CCTV_INFO[depth][1], CCTV_INFO[depth][2])
        dfs(depth+1, MAP)
        MAP = tmpMAP
    
def deepCopy(copy) :
    return [ item[:] for item in copy ]

if len(CCTV_INFO) != 0 :
    dfs(0, MAP)
else :
    tmpMin = 0
    for line in MAP :
        tmpMin += line.count(0)
    ans = tmpMin

print(ans)