# T = O(n)
# S = O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List(object):
    pass

def _print(head):
    if not head:
        return "List is empty"

    _head = head
    while _head:
        print(_head.data, end=" ")
        _head = _head.next
    print()

def middle_as_head(head):
    if not head:
        return
    slow = head
    fast = head
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = prev.next.next
    slow.next = head
    head = slow

    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

_print(head)
head = middle_as_head(head)
_print(head)
