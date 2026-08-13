class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(total, curr, i):
            if total > target:
                return
            elif total == target:
                res.append(curr.copy())
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                dfs(total + candidates[j], curr, j+1)
                curr.pop()
        dfs(0,[],0)
        return res
        