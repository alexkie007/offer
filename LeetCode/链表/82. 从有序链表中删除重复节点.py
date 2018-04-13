class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            temp = self.deleteDuplicates(head.next.next)
            if temp is not None and head.val == temp.val:
                head = temp.next
            else:
                head = temp
        return head