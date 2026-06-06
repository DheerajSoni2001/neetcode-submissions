class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        visited = set()
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            direc = [[1,0],[0,1],[-1,0],[0,-1]]
            while q:
                x,y = q.popleft()

                for dx,dy in direc:
                    nx,ny = x+dx,y+dy
                    if nx in range(row) and ny in range(col) and board[nx][ny] == "O" and (nx,ny) not in visited:
                        q.append((nx,ny))
                        visited.add((nx,ny))


        for i in range(row):
            if board[i][0] == "O":
                bfs(i,0)
            if board[i][col-1] == "O":
                bfs(i,col-1)
        
        for i in range(col):
            if board[0][i] == "O":
                bfs(0,i)
            if board[row-1][i] == "O":
                bfs(row-1,i)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
        

