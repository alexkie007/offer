class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def insertSort(self, Head):
        pass
    def selectSort(self, Head):
        return Head

    def quickSort(self, head):
        if not head or not head.next:
            return head
        self.quickSortCore(head,None)
        return head

    def partion(self, start, end):
        key = start.val
        p = start
        q = start
        while q != end:
            if q.val < key:
                p = p.next
                q.val, p.val = p.val, q.val
            q = q.next
        p.val, start.val = start.val, p.val
        return p

    def quickSortCore(self, start, end):
        if start == end or start.next == end:
            return
        mid = self.partion(start, end)
        self.quickSortCore(start, mid)
        self.quickSortCore(mid.next, end)

    def bubbleSort(self, Head):

        return Head

    def mergetSort(self, head):
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.mergetSort(head)
        r = self.mergetSort(second)
        return self.merge(l, r)

    def merge(self, l ,r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        head = LinkNode(l.val)
        head.next = self.merge(l.next, r)


        return head

a = LinkNode(2)
b = LinkNode(1)
c = LinkNode(3)
d = LinkNode(5)
e = LinkNode(4)
a.next = b
b.next = c
c.next = d
d.next = e
s =Solution()
# g = s.mergetSort(a)
g = s.quickSort(a)
while g:
    print(g.val)
    g = g.next