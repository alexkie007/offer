'''
输入一个链表的头节点，从尾到头反过来打印出每个节点的值
'''


class ListNode:
   def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode == None:
            return []
        stack = []
        while listNode !=None:
            stack.append(listNode.val)
            listNode = listNode.next
        return stack[::-1]

    def printListFromTailToHead2(self, listNode):
        if listNode == None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]
