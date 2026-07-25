class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append('#')
            res.append(word)
            
        res =''.join(res)
        print(res)
        return res
        
    def decode(self, s: str) -> List[str]:
        i =0
        res =[]
        while i < len(s):
            j = i
            while(s[j] != '#'):
                j+=1
            sz = int(s[i:j])
            i = j+1
            res.append(s[i:i+sz])
            i+=sz
        return res

        