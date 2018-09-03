class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def print_list_from_tail(self, head):
        if head is None:
            return []
        return self.print_list_from_tail(head.next) + [head.val]
