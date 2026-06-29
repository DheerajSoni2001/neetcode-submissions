class Solution:
    def tribonacci(self, n: int) -> int:
        i,j,k = 0,1,1
        dp = {}
        def dfs(n):
            if n==0:
                return 0
            if n==1 or n==2:
                return 1
            if n in dp:
                return dp[n]
            dp[n] = dfs(n-1)+dfs(n-2)+dfs(n-3)
            return dp[n] 
        return dfs(n)