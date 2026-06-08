class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        tickets.sort()

        for src,dst in tickets:
            graph[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res)==len(tickets)+1:
                return True
            if src not in graph:
                return False
            
            for i,val in enumerate(graph[src]):
                graph[src].pop(i)
                res.append(val)
                if dfs(val):
                    return True
                graph[src].insert(i,val)
                res.pop()
            return False   
        dfs("JFK")
        return res