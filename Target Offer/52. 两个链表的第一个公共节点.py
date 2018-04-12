'''
输入两个链表，找出它们的第一个公共节点
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # 遍历两个链表 找到公共节点 时间复杂度为O(n)
    def findfirstcommonnode1(self, node1, node2):
        if node1 == None or node2 == None:
            return None
        head2 = node2
        while node1:
            node2 = head2
            while node2:
                if node1.val == node2.val:
                    return node1
                elif node2:
                    node2 = node2.next
            node1 = node1.next
        return None

    def findfirstcommonnode2(self, node1, node2):
        if node1 == None or node2 == None:
            return None
        stack1 = []
        stack2 = []
        first = None
        while node1:
            stack1.append(node1)
            node1 = node1.next
        while node2:
            stack2.append(node2)
            node2 = node2.next
        while stack1 and stack2:
            top1 = stack1.pop()
            top2 = stack2.pop()
            if top1 == top2:
                first = top1
            else:
                continue
        return first


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(3)
node9 = ListNode(4)
node10 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10


s = Solution()
# while node1:
#     print(node1.val)
#     node1= node1.next
print(s.findfirstcommonnode2(node1, node6).val)



