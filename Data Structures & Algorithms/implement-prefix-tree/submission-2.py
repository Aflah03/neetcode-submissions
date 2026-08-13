class Node:
    def __init__(self):
        self.arr = [None] * 26
        self.terminal = False
class PrefixTree:

    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        temp = self.root
        for s in word:
            idx = ord(s) - ord('a')
            if temp.arr[idx] is None:
                temp.arr[idx] = Node()
            temp = temp.arr[idx]
        temp.terminal = True

    def search(self, word: str) -> bool:
        temp = self.root
        for s in word:
            idx = ord(s) - ord('a')
            if temp.arr[idx] is None:
                return False
            temp = temp.arr[idx]
        return temp.terminal 

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for s in prefix:
            idx = ord(s) - ord('a') 
            if temp.arr[idx] is None:
                return False
            temp = temp.arr[idx]
        return True
        