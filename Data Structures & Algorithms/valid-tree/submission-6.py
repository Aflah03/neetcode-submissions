class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)
        for x, y in  edges:
            mp[y].append(x)
            mp[x].append(y)
        
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for nei in mp[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n