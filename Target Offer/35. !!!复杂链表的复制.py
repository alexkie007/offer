'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return pHead
        self.cloneNode(pHead)
        self.connectNode(pHead)
        return self.reConnectNode(pHead)


    def cloneNode(self, pHead):
        while pHead:
            Cloned = RandomListNode(0)
            Cloned.label = pHead.label
            Cloned.next = pHead.next
            pHead.next = Cloned
            pHead = Cloned.next

    def connectNode(self, pHead):
        while pHead:
            Cloned = pHead.next
            if pHead.random:
                Cloned.random = pHead.random.next
            pHead = Cloned.next


    def reConnectNode(self, pHead):
        cloneHead = cloneNode = pHead.next
        pHead.next = cloneNode.next
        pHead = pHead.next
        while pHead:
            cloneNode.next = pHead.next
            cloneNode = pHead.next
            pHead.next = cloneHead.next
            pHead = pHead.next
        return cloneHead



