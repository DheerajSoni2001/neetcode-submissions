class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)

        for x,y,val in flights:
            graph[x].append((y,val))

        min_cost = [float('inf')] * n
        min_cost[src] = 0
        
        q = collections.deque()
        q.append((src,0))
        stops = 0
        
        while q and stops <= k:
            size = len(q)
            for _ in range(size):
                ele, cost_node1 = q.popleft()

                for neigh, cost_node2 in graph[ele]:
                    new_cost = cost_node1 + cost_node2

                    if new_cost < min_cost[neigh]:
                        min_cost[neigh] = new_cost
                        q.append((neigh,new_cost))
            stops += 1

        return int(min_cost[dst]) if min_cost[dst] != float('inf') else -1