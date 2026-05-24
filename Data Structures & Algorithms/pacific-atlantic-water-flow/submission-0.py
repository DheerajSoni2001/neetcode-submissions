class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        #1->Pacific   2->Atlantic
        p = set()
        a = set()
        direc = [[1,0], [0,1], [-1,0], [0,-1]]

        def bfs(r,c,visited):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                x,y = q.popleft()

                for dx,dy in direc:
                    nx,ny = x+dx, y+dy
                    if nx in range(row) and ny in range(col) and heights[nx][ny] >= heights[x][y] and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        q.append((nx,ny))


        for j in range(col):
            bfs(0,j,p)
            bfs(row-1, j,a)
        
        for i in range(row):
            bfs(i,0,p)
            bfs(i,col-1,a)

        return [list(x) for x in p & a]

            