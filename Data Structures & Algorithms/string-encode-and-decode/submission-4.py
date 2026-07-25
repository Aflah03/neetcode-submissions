class Solution:

    def encode(self, strs: List[str]) -> str:
        res, sizes = [], []
        for s in strs:
            sizes.append(len(s))
        for s in sizes:
            res.append(str(s))
            res.append(',')
        res.append('#')
        for s in strs:
            res.append(s)
        res  = ''.join(res)
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j+=1
            sizes.append(int(s[i:j]))
            i = j+1
        i+=1
        for sz in sizes:
            res.append(s[i:i+sz])
            i+=sz
        return res
        