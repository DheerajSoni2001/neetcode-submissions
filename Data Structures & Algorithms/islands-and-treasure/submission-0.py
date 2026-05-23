class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        direc = [[1,0], [-1,0], [0,1], [0,-1]]
        INF = 2147483647

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited = set()
            visited.add((i, j))
            while q:
                x, y = q.popleft()
                for dx, dy in direc:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < len(grid) and
                        0 <= ny < len(grid[0]) and
                        grid[nx][ny] != -1 and
                        (nx, ny) not in visited):
                        grid[nx][ny] = min(grid[nx][ny], grid[x][y] + 1)  # ✅ take min
                        visited.add((nx, ny))
                        q.append((nx, ny))

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 0:
                    bfs(i, j)