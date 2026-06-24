class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if dp[i][j] != 0:
                return dp[i][j]
            down = right = 0
            right += dfs(i,j+1)
            down += dfs(i+1,j)
            dp[i][j] = down + right
            return dp[i][j]
        ans = dfs(0,0)
        return ans