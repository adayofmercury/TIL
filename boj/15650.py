import sys

input = sys.stdin.readline

n, m = map(int,input().split())

li =[]
nums = [i for i in range(1, n+1)]

def dfs(index, li, nums) :
    for i in range(index, len(nums)) :
        li.append(nums[i])
        i += 1
        if len(li) == m :
            for _ in li :
                print(_ , end = ' ')
            print()
        else :
            #print('---','dfs',i,li)
            dfs(i, li, nums)
        
        #print(i,li, 'pop')
        li.pop()

dfs(0, li, nums)



## 얻어걸렸는데 다시 분석해 볼 필요가 있음..
## 