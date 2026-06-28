class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(i,j):
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            if (i,j) in dp:
                return dp[(i,j)]

            match = i < len(s) and j < len(p) and (s[i]==p[j] or p[j]=='.')
            ans = False
            if match:
                ans = dfs(i+1,j+1)
            if (j+1)<len(p) and p[j+1]=='*':
                ans = dfs(i,j+2) or (match and dfs(i+1,j))
            dp[(i,j)] = ans
            return dp[(i,j)]

        return dfs(0,0)