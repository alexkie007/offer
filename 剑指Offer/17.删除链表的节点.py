class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


def deleteNode(head, p):
    if not p or not head:
        return None

    if p.next != None:
        pNext = p.next
        p.val = pNext.val
        p.next = pNext.next

        pNext.__del__()

    elif head == p:
        p.__del__()
        head.__del__()
    else:
        pNode = head
        while pNode != p:
            pNode = pNode.next
        pNode.next = None
        p.__del__()

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4


deleteNode(node1, node3)
print(node3.val)
deleteNode(node1, node3)
print(node3.val)
print(node2.val)
deleteNode(node1, node1)
print(node1.val)
deleteNode(node1, node1)
print(node1.val)