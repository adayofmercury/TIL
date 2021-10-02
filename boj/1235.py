from collections import defaultdict
import sys

input = sys.stdin.readline


def solve(studentsList, cnt) :
    new_keyDict = defaultdict(str)
    for i in studentsList :
        new_key = i[-cnt:]
        if new_key in new_keyDict.keys() :
            return solve(studentsList, cnt+1)
        else :
            new_keyDict[new_key] = 1
    print(cnt)
    #print(new_keyDict)

if __name__ == '__main__' :
    studentsList = []
    for N in range(int(input())) :
        studentsList.append(input().rstrip())
    solve(studentsList, 1)
