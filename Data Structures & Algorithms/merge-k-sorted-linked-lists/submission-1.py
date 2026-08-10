# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)== 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                ans = res = ListNode()
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                while list1 and list2:
                    if list1.val <= list2.val:
                        ans.next = list1
                        list1 = list1.next
                    else:
                        ans.next = list2
                        list2  = list2.next
                    ans = ans.next
                ans.next = list1 or list2
                mergedLists.append(res.next)
            lists = mergedLists
        return lists[0]
    
        