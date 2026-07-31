class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        a1 = [0] * 128
        a2 = [0] *128
        for i in range(len(s1)):
            a1[ord(s1[i])]+=1
            a2[ord(s2[i])]+=1
        for i in range(len(s1), len(s2)):
            if a1 == a2:
                return True
            a2[ord(s2[i])]+=1
            a2[ord(s2[i-len(s1)])]-=1
        return a1 == a2