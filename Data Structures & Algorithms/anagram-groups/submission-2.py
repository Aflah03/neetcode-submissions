class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for word in strs:
            sortedS = ''.join(sorted(word))
            mp[sortedS].append(word)
        res = []
        for key, value in mp.items():
            res.append(value)
        return res