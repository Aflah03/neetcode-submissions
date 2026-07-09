class Solution:
    def checkValidString(self, s: str) -> bool:
        mini =0
        maxi = 0
        for i in range(len(s)):
            if(s[i] == '('):
                mini +=1
                maxi+=1
            if(s[i]== ')'):
                mini-=1 
                if mini < 0:
                    mini = 0
                maxi-=1
            if  maxi < 0:
                return False
            if(s[i] == '*'):
                mini -=1
                if mini < 0: mini = 0
                maxi +=1
        if mini == 0:
            return True
        return False