class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def linked_list(array:list) -> ListNode:
    head = None
    cursor = head
    for n in array:
        node = ListNode(n)
        if not head:
            head = node
            cursor = node
        else:
            cursor.next = node
            cursor = node
    return head

def print_linked_list(head:ListNode):
    while head:
        print(head.val)
        head = head.next