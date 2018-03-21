'''
输入一个链表，反转链表后，输出链表的所有元素。
'''
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead ==None or pHead.next == None:
            return pHead
        last = None
        while pHead:
            temp = pHead.next
            pHead.next = last
            last = pHead
            pHead = temp
        return last   