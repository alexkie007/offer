'''
一个链表中包含环，请找出该链表的环的入口结点。

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def EntryNodeOfLoop(self, pHead):
        # 先看有没有回路
        meetingNode = self.Loop(pHead)
        if not meetingNode:
            return None
        # 找到环的长度
        NodeLoop = 1
        pFast = meetingNode.next
        while pFast != meetingNode:
            NodeLoop += 1
            pFast = pFast.next
        # 前面的先走n步 碰到后面的即是入口
        pFast = pHead
        for i in range(NodeLoop):
            pFast = pFast.next
        pSlow = pHead
        while pSlow != pFast:
            pSlow = pSlow.next
            pFast = pFast.next

        return pFast

    def Loop(self, pHead):
        if not pHead:
            return pHead
        pSlow = pHead.next
        if not pSlow:
            return None
        pFast = pSlow.next

        while pFast:
            if pFast == pSlow:
                return pSlow

            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next
        return None
