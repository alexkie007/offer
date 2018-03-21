'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def merge(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1

        pMergeHead = None

        if head1.val < head2.val:
            pMergeHead = head1
            pMergeHead.next = self.merge(head1.next, head2)
        else:
            pMergeHead = head2
            pMergeHead.next = self.merge(head1, head2.next)

        return pMergeHead


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

S = Solution()
S.merge(node1, node4)
print(node4.next.val)