class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        q = collections.deque()
        q.append((0,-1))
        visited.add(0)

        while q:
            x,p = q.popleft()

            for neigh in graph[x]:
                if neigh in visited and neigh != p:
                    return False
                if neigh == p:
                    continue
                visited.add(neigh)
                q.append((neigh,x))

        return len(visited)==n

        