import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input())
ver = defaultdict(str)

for _ in range(n) :
    root, left, right = input().rstrip().split()
    ver[root] = [left, right]

#print(ver)
li = []

def p(li) :
    for _ in li :
        print(_, end='')
    print()

def first(index) :
    li.append(index)
    if ver[index][0] != '.' :
        first(ver[index][0])
    if ver[index][1] != '.' :
        first(ver[index][1])

first('A')
p(li)
li = []

def mid(index) :
    if ver[index][0] != '.' :
        mid(ver[index][0])
    li.append(index)
    if ver[index][1] != '.' :
        mid(ver[index][1])

mid('A')
p(li)
li = []

def end(index) :
    if ver[index][0] != '.' :
        end(ver[index][0])
    if ver[index][1] != '.' :
        end(ver[index][1])
    li.append(index)
    
end('A')
p(li)
