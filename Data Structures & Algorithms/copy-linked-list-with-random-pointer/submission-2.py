"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        temp = head
        while temp:
            nxt = temp.next
            temp.next = Node(temp.val)
            temp = temp.next
            temp.next= nxt
            temp = temp.next
        prev = head
        curr = head.next
        while prev:
            if prev.random:
                curr.random = prev.random.next
            prev = curr.next
            if prev is None:
                break
            curr = prev.next
        prev = head
        curr = head.next
        ans = curr
        while prev:
            nxt = curr.next
            if nxt is not None:
                curr.next = nxt.next
            prev.next = nxt
            prev= nxt
            if nxt is not None: 
                curr = nxt.next
        return ans
        