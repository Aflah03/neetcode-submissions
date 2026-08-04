# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # nodes = []
        # temp = head
        # while temp:
        #     nodes.append(temp)
        #     temp = temp.next
        # l = 0
        # r = len(nodes)-1
        # while l< r:
        #     nodes[l].next = nodes[r]
        #     l+=1
        #     # if l >=r: 
        #     #     break
        #     nodes[r].next = nodes[l]
        #     r-=1
        # nodes[l].next = None
        if head.next is None:
            return 
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None #cut the LL in half

        # slow is the new head , we want to reverse it 
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr =nxt
        head2 = prev
        res = ans = ListNode()
        list1 = head
        list2 = head2
        while list1 and list2:
            res.next = list1
            list1 = list1.next
            res = res.next
            res.next = list2
            list2 = list2.next
            res = res.next
        res.next =list1 or list2
        head = res.next
        