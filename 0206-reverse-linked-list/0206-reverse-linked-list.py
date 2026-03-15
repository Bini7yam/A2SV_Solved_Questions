# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        past = None
        while cur:
            nxt = cur.next
            cur.next = past
            past = cur
            cur = nxt
        return past
        