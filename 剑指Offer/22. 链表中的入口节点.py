'''
一个链表中包含环，请找出该链表的环的入口结点。
先确定是否有环
然后确定环的节点数量
再找入口节点
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def meetingNone(self, head):
        if head == None:
            return None

        pSlow = head.next
        if pSlow == None:
            return None
        pFast = pSlow.next
        while pFast:
            if pSlow == pFast:
                return pSlow
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next
        return None

    def EntryNodeofLoop(self, head):
        meetingNode = self.meetingNone(head)
        if not meetingNode:
            return None

        # 找到环的节点数目
        NodeLoop =1
        flagNode = meetingNode
        while flagNode.next != meetingNode:
            NodeLoop += 1
            flagNode = flagNode.next

        #
        pFast = head
        for i in range(NodeLoop):
            pFast = pFast.next
        pSlow = head
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.EntryNodeofLoop(node1).val)
