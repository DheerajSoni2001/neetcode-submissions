class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        dp = {}
        def dfs(i,goal):
            if i<0:
                return float('inf')
            if i==0: 
                if nums[0] >= goal:
                    return 1
                else:
                    return float('inf')
            if (i,goal) in dp:
                return dp[(i,goal)]
            #include
            inc = float('inf')
            if(i+nums[i] >= goal):
                inc = 1+dfs(i-1,i)
            exc = dfs(i-1,goal)
            dp[(i,goal)] = min(inc,exc)
            return min(inc,exc)
        return dfs(len(nums)-2,len(nums)-1)
