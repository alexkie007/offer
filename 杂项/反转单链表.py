class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, node):
        if node ==None or node.next == None:
            return node
        last = None
        while node:
            temp = node.next
            node.next = last
            last = node
            node = temp
        return last

a = ListNode(3)
b = ListNode(1)
c = ListNode(4)
d = ListNode(2)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
s = Solution()
g = s.reverseList(a)
while g:
    print(g.val)
    g = g.next
