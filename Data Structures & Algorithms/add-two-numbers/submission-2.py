# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c =0
        temp1 = l1
        temp2 = l2
        ans = res = ListNode()
        while temp1 and temp2:
            summ = temp1.val + temp2.val + c
            ans.next= ListNode(summ%10)
            ans = ans.next
            temp1 = temp1.next
            temp2 = temp2.next
            c = summ//10
        while temp1:
            summ = temp1.val + c
            ans.next= ListNode(summ%10)
            ans = ans.next
            temp1 = temp1.next
            c = summ//10
        while temp2:
            summ = + temp2.val + c
            ans.next= ListNode(summ%10)
            temp2 = temp2.next
            ans = ans.next
            c = summ//10
        if c:
            ans.next = ListNode(1)
            ans = ans.next
        return res.next


