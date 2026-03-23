# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while arr[-1].next:
            now = arr[-1].next
            while arr and arr[-1].val < now.val:
                arr.pop()
            if arr: arr[-1].next = now
            arr.append(now)
        return arr[0]
            
            
        