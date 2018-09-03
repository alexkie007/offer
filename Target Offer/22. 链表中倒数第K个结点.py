'''
输入一个链表，输出该链表中倒数第k个结点。
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if k <= 0:
            return
        if head == None:
            return
        pFront = head
        pBehind = head
        for i in range(k - 1):
            if pFront.next != None:
                pFront = pFront.next
            else:
                return None
        while pFront.next != None:
            pFront = pFront.next
            pBehind = pBehind.next
        return pBehind
