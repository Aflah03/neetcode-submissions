class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        mp = defaultdict(list)
        for x, y in edges:
            mp[x].append(y)
            mp[y].append(x)
        def dfs(node):
            for nei in mp[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
        res = 0
        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                res+=1
        return res