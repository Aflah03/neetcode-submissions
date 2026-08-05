# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        temp1 = l1
        temp2 = l2
        res = ListNode()
        ans  =res
        while temp1 and temp2:
            res.next = ListNode()
            res = res.next
            summ = (temp1.val + temp2.val+c)
            res.val = summ % 10
            c = summ //10
            print("first looop: ", c)
            
            temp1 = temp1.next
            temp2  =temp2.next
        while temp1:
            res.next = ListNode()
            res = res.next
            summ = (temp1.val + c)
            c = summ//10
            res.val = summ%10
            print(c)
            
            temp1 = temp1.next
        while temp2:
            res.next = ListNode()
            res = res.next
            summ = (temp2.val + c)
            c = summ//10
            print("temp2 loop: ", c)
            res.val = summ%10
            
            temp2 = temp2.next
        if c:
            res.next = ListNode()
            res = res.next
            res.val = c
        return ans.next
        
            

        