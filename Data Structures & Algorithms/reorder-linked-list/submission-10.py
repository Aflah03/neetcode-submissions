class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return

        arr = []
        temp = head

        while temp:
            arr.append(temp)
            temp = temp.next

        n = len(arr)

        i, j = 0, len(arr)-1
        while i < j:
            arr[i].next = arr[j]
            i+=1
            if i>=j:
                break
            arr[j].next = arr[i]
            j-=1
        arr[i].next= None
