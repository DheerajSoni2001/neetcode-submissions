class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        def dfs(i,val):
            if i == len(nums):
                return 1 if val==target else 0
            if (i,val) in dp:
                return dp[(i,val)]
            add = dfs(i+1, val+nums[i])
            sub = dfs(i+1, val-nums[i])
            dp[(i,val)] = add+sub
            return dp[(i,val)]
        
        return dfs(0,0)