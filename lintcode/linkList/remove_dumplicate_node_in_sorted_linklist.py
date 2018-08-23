class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    @staticmethod
    def remove_dup_node(head):
        if head is None or head.next is None:
            return head
        dummy = Node(None)
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            if head.next.val == head.next.next.val:
                val = head.next.val
                while head.next and head.next.val == val:
                    head.next = head.next.next
            else:
                head = head.next
        return dummy.next

    @staticmethod
    def remove_dup_node_2(head):
        if head is None or head.next is None:
            return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


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
head = s.remove_dup_node(a)
while head:
    print(head.val)
    head = head.next

head = s.remove_dup_node_2(a)
while head:
    print(head.val)
    head = head.next