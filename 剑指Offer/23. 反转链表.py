'''
反转链表
输入一个链表，反转链表后，输出链表的所有元素
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def ReverseList(self, head):
        if not head or not head.next:
            return head
        then = head.next
        head.next = None
        last = then.next
        while then:
            then.next = head
            head = then
            then = last
            if then:
                last = then.next
        return head


    def ReverseListRec(self, head):
        if not head or not head.next:
            return head
        else:
            pReversedHead = self.ReverseList(head.next)
            head.next.next = head
            head.next = None
            return pReversedHead

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
p = S.ReverseList(node1)
print(p.val)