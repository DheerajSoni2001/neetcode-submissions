import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visit = set()
        res = 0
        minheap = []
        heapq.heappush(minheap, (0,points[0][0],points[0][1]))
        while minheap and len(visit) != len(points):
            w,x1,y1 = heapq.heappop(minheap)
            if (x1,y1) in visit:
                continue
            visit.add((x1,y1))
            res += w
            for x2,y2 in points:
                if (x2,y2) not in visit:
                    dist = abs(x2-x1)+abs(y2-y1)
                    heapq.heappush(minheap,(dist,x2,y2))
        return res
