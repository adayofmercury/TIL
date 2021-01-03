import sys
input = sys.stdin.readline

li = []
for _ in range(int(input())) :
    li.append(list(map(int,input().split())))

li.sort(key = lambda x: (x[0], x[1]))

#print(li)
start = li[0][0]
end = li[0][1]
count = 0
for x, y in li :
    if count == 0 and x == li[0][0] and y == li[0][1] : #첫번째 거에 대한 예외처리
        count += 1
        continue
    if x == end and y == end : # 처음과 끝이 같은 경우 깍두기
        count += 1
    if start <= x and y <= end : # start 와 end 를 바꾸는 과정
        start = x
        end = y
    elif end <= x :
        start = x
        end = y
        count += 1

print(count)


# sorting 해서 시작점과 끝점을 이동시키는 아이디어로 해결 