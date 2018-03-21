class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    def print_list(self, listNode):
        if listNode.val == None:
            return False
        l = []

        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l


if __name__ == '__main__':
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3
    S = Solution()
    print(S.print_list(node1))