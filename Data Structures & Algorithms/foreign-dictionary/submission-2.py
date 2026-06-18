class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)

        for x,y in zip(words,words[1:]):
            minlen = min(len(x), len(y))
            if len(x) > len(y) and x[:minlen]==y[:minlen]:
                return ""
            for i in range(minlen):
                if x[i] != y[i]:
                    graph[x[i]].append(y[i])
                    break
        
        indegree = { char:0 for word in words for char in word }
        for x in graph:
            for y in graph[x]:
                indegree[y] += 1
        
        q = collections.deque()


        for x in indegree:
            if indegree[x]==0:
                q.append(x)
        
        ans = ""
        while q:
            ele = q.popleft()
            ans += ele
            for neigh in graph[ele]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        for x in indegree:
            if indegree[x] != 0:
                return ""

        return ans







