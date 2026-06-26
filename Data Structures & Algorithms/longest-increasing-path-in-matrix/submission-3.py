class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        dp = {}

        def dfs(r,c,val):
            if matrix[r][c] <= val:
                return 0

            if (r,c) in dp:
                return dp[(r,c)]

            count = 0
            direc = [[1,0],[0,1],[-1,0],[0,-1]]
            for dx,dy in direc:
                nx,ny = r+dx,c+dy
                if nx in range(row) and ny in range(col):
                    count = max(count,dfs(nx,ny,matrix[r][c]))

            dp[(r,c)] = 1 + count
            
            return dp[(r,c)]


        maxi = -1
        for i in range(row):
            for j in range(col):
                maxi = max(maxi,dfs(i,j,-1))
        
        return maxi
            