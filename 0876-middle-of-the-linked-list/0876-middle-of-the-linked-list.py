# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = mid = head
        d = 1
        while last:
            last = last.next
            if not last:break
            if d: mid = mid.next
            d = 1 - d
        return mid
        