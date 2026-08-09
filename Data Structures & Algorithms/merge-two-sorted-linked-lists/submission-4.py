# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        ans = ListNode()
        res = ans
        while temp1 and temp2:
            if temp1.val < temp2.val:
                ans.next = temp1
                temp1 = temp1.next
                ans = ans.next
            else:
                ans.next = temp2
                temp2 = temp2.next
                ans = ans.next
        ans.next  = temp1 or temp2
        return res.next