class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteNode(self, pHead, pNode):
        if not pHead or not pNode:
            return
        if pNode == pHead:
            pHead = pHead.next
        elif pNode.next != None:
            pNode.val = pNode.next.val
            pNode.next = pNode.next.next
        else:
            Node = pHead
            while Node.next != pNode:
                Node = Node.next
            Node.next = None
        return pHead
