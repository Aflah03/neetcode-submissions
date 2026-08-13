class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1 = [0] * 2048
        mp2 = [0] * 2048
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            mp1[ord(s1[i])] +=1
            mp2[ord(s2[i])] +=1
        for i in range(len(s1), len(s2)):
            if mp1 == mp2:
                return True
            mp2[ord(s2[i])]+=1
            mp2[ord(s2[i-len(s1)])] -=1
        return mp1 == mp2
        return False