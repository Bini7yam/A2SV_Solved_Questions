# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        ehead = head.next
        odd = head
        evn = head.next
        while evn and evn.next:
            odd.next = evn.next
            odd = odd.next
            evn.next = odd.next
            evn = evn.next
        odd.next = ehead
        return head
        