class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(left,right):
            if left+1==right:
                return 0
            if (left,right) in dp:
                return dp[(left,right)]
            ans = 0
            for k in range(left+1,right):
                coins = (nums[left]*nums[k]*nums[right] + dfs(left,k) + dfs(k,right))
                ans = max(coins,ans)
            dp[(left,right)] = ans
            return dp[(left,right)]
        return dfs(0,len(nums)-1)