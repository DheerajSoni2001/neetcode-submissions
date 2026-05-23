class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        max_area=0
        def bfs(i,j):
            area=0
            q=[]
            q.append((i,j))
            directions=[[1,0],[0,1],[-1,0],[0,-1]]
            while(q):
                area+=1
                x,y=q.pop(0)
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx in range(row) and ny in range(col) and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        q.append((nx,ny))
            return area

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    grid[i][j]=2
                    max_area=max(bfs(i,j), max_area)
        return max_area
