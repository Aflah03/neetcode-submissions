# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        temp = head
        while temp:
            if temp in nodes:
                return True
            nodes.add(temp)
            temp = temp.next
        return False