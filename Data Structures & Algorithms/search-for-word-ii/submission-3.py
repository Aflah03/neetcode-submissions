class Node:
    def __init__(self):
        self.arr = [None]*26
        self.terminal = False
class Solution:
    def __init__(self):
        self.root= Node()
    def addWord(self, word):
        temp = self.root
        for c in word:
            idx = ord(c)- ord('a')
            if temp.arr[idx] is None:
                temp.arr[idx] = Node()
            temp = temp.arr[idx]
        temp.terminal = True
     
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        m= len(board)
        n = len(board[0])
        for word in words:
            self.addWord(word)
        
        def dfs(r,c,root,visit, word):
            if root is None:
                return False
            if root.terminal:
                res.append(word)
                root.terminal = False
            

            
            for d in dirs:
                rr= r+d[0]
                cc = c+d[1]
                if rr>=0 and cc >= 0 and cc <n and rr <m and (rr,cc) not in visit: 
                    idx = ord(board[rr][cc]) - ord('a') 
                    visit.add((rr,cc))
                    
                    dfs(rr,cc,root.arr[idx],visit,word+board[rr][cc])
                    # print(word)
                    visit.remove((rr,cc))
        
        for r in range(m):
            for c in range(n):
                idx = ord(board[r][c]) - ord('a')
                if self.root.arr[idx]:
                    dfs(r,c,self.root.arr[idx],{(r,c)},board[r][c])
                 
        return res
        
        