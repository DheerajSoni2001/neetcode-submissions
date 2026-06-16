import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        mini = grid[n-1][m-1]
        visit = set()
        minheap = []
        heapq.heappush(minheap, (grid[n-1][m-1], n-1, m-1))
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        while minheap:
            ele,x,y = heapq.heappop(minheap)
            mini = max(mini,ele)
            if x==0 and y==0:
                break
            for dx,dy in direction:
                nr,nc = x+dx, y+dy
                if nr in range(n) and nc in range(m) and (nr,nc) not in visit:
                    heapq.heappush(minheap,(grid[nr][nc],nr,nc))
                    visit.add((nr,nc))

        return mini
        