# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) ==0:
            return None
        def mergeLL(l1,l2):
            dummy = res = ListNode()
            if not l1:
                return l2
            if not l2:
                return l1
            while l1 and l2:
                if l1.val <= l2.val:
                    res.next = l1
                    l1 = l1.next
                else:
                    res.next = l2
                    l2 = l2.next
                res = res.next
            res.next = l1 or l2 or None
            return dummy.next
        while len(lists) > 1:
            merged = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 <len(lists) else None
                merged.append(mergeLL(l1,l2))
            lists = merged
        return lists[0]

