'''
输入一个
复杂链表（每个节点中有节点值，以及两个指针，
一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
'''

# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def Clone(self, head):
        if head == None:
            return head
        self.CloneNodes(head)
        self.ConnetRandomNodes(head)
        return self.ReconnectNodes(head)

    def CloneNodes(self, head):
        Node = head
        while Node:
            Cloned = RandomListNode(0)
            Cloned.label = Node.label
            Cloned.next = Node.next

            Node.next = Cloned
            Node = Cloned.next

    def ConnetRandomNodes(self, head):
        Node = head
        while Node:
            Cloned = Node.next
            if Node.random != None:
                Cloned.random = Node.random.next
                Node = Cloned.next

    def ReconnectNodes(self, head):
        Node = head
        CloneHead = CloneNode = Node.next
        Node.next = CloneHead.next
        Node = Node.next
        while Node:
            CloneHead.next= Node.next
            CloneHead = CloneNode.next
            Node.next = CloneHead.next
            Node = Node.next

        return CloneHead


node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)