'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。
 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
 '''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def deleteDuplication(self, pHead):
        if not pHead:
            return pHead
        res = []
        while pHead:
            res.append(pHead.val)
            pHead = pHead.next
        res = list(filter(lambda c: res.count(c) == 1, res))
        dumpy = ListNode(0)
        pre = dumpy
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return dumpy.next


class Solution2:
    def deleteDuplication(self, pHead):
        dummy = ListNode(None)
        dummy.next = pHead
        curr = dummy
        while curr:
            has_dup = False
            # Remove duplicates and leave the last of the duplicates.
            while curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                curr.next = curr.next.next
                has_dup = True
            if has_dup:
                # Remove the last duplicate
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


a = ListNode(1)
b = ListNode(1)
c = ListNode(1)
d = ListNode(2)
e = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = e

s = Solution2()
print(s.deleteDuplication(a))


class Solution3:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            # 首先判断是否为空，或是否只有一个结点。
            return pHead
        if pHead.val != pHead.next.val:
            # 如果当前结点值不等于下一结点值，则该结点保留并返回
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            # 否则从下一个结点开始寻找下一个不重复的结点。找到后返回，并判断是否与当前结点相等。
            temp = self.deleteDuplication(pHead.next.next)
            if temp is not None and pHead.val == temp.val:
                pHead = None
            else:
                pHead = temp
        return pHead
