class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = {}

        def dfs(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            include = exclude = 0
            if s[i]==t[j]:
                include += dfs(i+1,j+1)
                exclude += dfs(i+1,j)
            else:
                return dfs(i+1,j)
            dp[(i,j)] = include + exclude
            return dp[(i,j)]

        return dfs(0,0)
