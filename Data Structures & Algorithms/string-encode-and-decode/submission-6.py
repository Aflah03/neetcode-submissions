class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res +=str(len(s))
            res+='#'
            res+=s
        res = ''.join(res)
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        i =0
        res = []
        while i < len(s):
            j = i
            while j  < len(s) and s[j] != '#':
                j+=1
            l = int(s[i:j])
            i = j
            i+=1
            res.append(s[i:i+l])
            i = i+l
        return res


