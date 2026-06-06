class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        row = len(edges)
        col = len(edges[0])

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        count = 0
        
        def dfs(i):
            if i in visited:
                return    
            visited.add(i)
            for neigh in graph[i]:
                dfs(neigh)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count