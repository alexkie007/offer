class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    @staticmethod
    def reverse_list(head):
        if head is None or head.next is None:
            return head
        dummy = Node(None)
        while head:
            temp = head.next
            head.next = dummy
            dummy = head
            head = temp
        return dummy


a = Node(1)
b = Node(1)
c = Node(1)
d = Node(2)
e = Node(2)
f = Node(3)
g = Node(4)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
s = Solution()
head = s.reverse_list(a)
while head.val:
    print(head.val)
    head = head.next

