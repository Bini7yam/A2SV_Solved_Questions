class node:
    def __init__(self, x = 0):
        self.val = x
        self.next = None
        self.prev = None
class MyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        

    def get(self, index: int) -> int:
        cur = self.head
        while cur and index:
            cur = cur.next
            index -= 1
        return cur.val if cur else -1
        

    def addAtHead(self, val: int) -> None:
        temp = node(val)
        if not self.head:
            self.head = self.tail = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def addAtTail(self, val: int) -> None:
        temp = node(val)
        if not self.head:
            self.head = self.tail = temp
            return
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        

    def addAtIndex(self, index: int, val: int) -> None:
        temp = node(val)
        if not index:
            self.addAtHead(val)
            return
        index -= 1
        cur = self.head
        while cur and index:
            cur = cur.next
            index -= 1
        if not cur: return
        if not cur.next:
            self.addAtTail(val)
            return
        nxt = cur.next
        cur.next = temp
        temp.prev = cur
        temp.next = nxt
        nxt.prev = temp
        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head: return
        if not index:
            self.head = self.head.next
            return
        cur = self.head
        while cur and index:
            cur = cur.next
            index -= 1
        if not cur: return
        cur.prev.next = cur.next
        if cur.next: cur.next.prev = cur.prev
        else: self.tail = cur.prev

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)