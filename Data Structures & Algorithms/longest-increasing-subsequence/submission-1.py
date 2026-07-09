class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i,j):
            if i==len(nums):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            exc = dfs(i+1,j)
            inc = 0
            if j==-1 or nums[i]>nums[j]:
               inc = 1 + dfs(i+1,i)
            dp[(i,j)] = max(exc,inc)
            return dp[(i,j)]
        return dfs(0,-1)