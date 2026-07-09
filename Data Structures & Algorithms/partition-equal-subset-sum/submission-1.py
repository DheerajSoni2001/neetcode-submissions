class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2:
            return False
        dp = {}
        def dfs(i,half):
            if half == 0:
                return True
            if i==len(nums):
                return False
            if (i,half) in dp:
                return dp[(i,half)]
            exc = dfs(i+1,half)
            inc = False
            if nums[i] <= half:
                inc = dfs(i+1,half-nums[i])
            dp[(i,half)] = exc or inc
            return exc or inc
        return dfs(0,sum(nums)//2)
