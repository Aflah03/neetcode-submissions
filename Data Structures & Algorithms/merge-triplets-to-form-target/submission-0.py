class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()
        for t in triplets:
            allowed = True
            for i in range(0,3):
                if t[i] > target[i]:
                    allowed = False
            if allowed:
                for i in range(0,3):
                    if t[i] == target[i]:
                        res.add(i)
        return len(res) == 3