import sys

input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n) :
    words.append(input().rstrip())



words = set(words)
words = list(words)

words.sort(key = lambda x : (len(x), x))

for _ in words :
    print(_)