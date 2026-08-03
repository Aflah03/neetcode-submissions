# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return 
        if head.next is None:
            return 
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        curr = slow
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # temp1 = prev
        # temp2 = head
        # # print("The second list")
        # while temp1:
        #     print(temp1.val)
        #     temp1 = temp1.next
        # print("The first list")
        # while temp2:
        #     print(temp2.val)
        #     temp2 = temp2.next
        list2 = prev
        list1 = head
        res = ListNode()
        ans = res
        while list1 and list2:
            res.next = list1
            list1 = list1.next
            res = res.next
            res.next = list2
            list2 = list2.next
            res = res.next
        res.next = list1 or list2
        head = ans.next
           

