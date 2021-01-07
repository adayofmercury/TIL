n, m = map(int,input().split())

nums = list(map(int,input().split()))

nums.sort()

li = []

def dfs(index, li, nums) :
    
    for i in range(index, len(nums)) :
        li.append(nums[i])
        if len(li) == m :
            for _ in li :
                print(_, end= ' ')
            print()

        else :
            dfs(i, li, nums)
        
        li.pop()

dfs(0, li, nums)