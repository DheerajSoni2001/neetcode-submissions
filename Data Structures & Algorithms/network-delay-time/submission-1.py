import heapq
from collections import defaultdict
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for x,y,t in times:
            graph[x].append([y,t])
        
        visited = set()
        minheap = [(0,k)]
        t = 0
        

        while minheap:
            w, val = heapq.heappop(minheap)
            if val in visited:
                continue
            visited.add(val)
            t = max(t,w)

            for neigh, w1 in graph[val]:
                if neigh not in visited:
                    heapq.heappush(minheap, (w1+w, neigh))

        return t if len(visited)==n else -1
