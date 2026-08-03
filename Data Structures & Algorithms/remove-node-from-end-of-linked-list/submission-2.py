# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes =[]
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next
        if len(nodes)-n ==0:
            return head.next
        nodes[len(nodes)-n-1].next = nodes[len(nodes)-n].next
        return head