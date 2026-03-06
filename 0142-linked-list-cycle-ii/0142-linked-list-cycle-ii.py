# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vs = set()
        cur = head
        while cur:
            if cur in vs: return cur
            vs.add(cur)
            cur = cur.next
        return None