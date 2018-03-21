class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


def deleteDuplicates(head):
    if head is None:
        return head
    record = set()
    record.add(head.val)
    cur, pre = head.next, head
    while cur:
        if cur.val in record:
            pre.next = cur.next
            cur = cur.next
            if pre == head:
                head = cur.next
        else:
            record.add(cur.val)
            pre= pre.next
            cur= cur.next
    return head


node1 = ListNode(10)
node2 = ListNode(10)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4

deleteDuplicates(node1)
print(node1.val)
print(node2.val)
print(node3.val)
print(node4.val)