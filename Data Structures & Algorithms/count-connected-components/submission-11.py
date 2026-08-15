class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            mp[u].append(v)
            mp[v].append(u)
        def bfs(node):
            q = deque([node])
            while q:
                cur = q.popleft()
                for nei in mp[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)
        res = 0
        for node in range(n):
            if not  visit[node]:
                visit[node] = True
                bfs(node)
                res+=1
        return res