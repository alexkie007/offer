'''
输入一个链表，反转链表后，输出链表的所有元素。
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead ==None or pHead.next == None:
            return pHead
        last = None
        while pHead:
            temp = pHead.next
            pHead.next = last
            last = pHead
            pHead = temp
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
g = s.ReverseList(a)
while g:
    print(g.val)
    g = g.next