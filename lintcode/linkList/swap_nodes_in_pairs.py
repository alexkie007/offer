class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def swap_pairs(head):
    dummy =  ListNode(None)
    dummy.next = head
    pre = dummy
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        a.next = b.next
        b.next = a
        pre.next = b
        pre = a
    return dummy.next