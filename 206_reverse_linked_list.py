from common import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        # use a variable to keep the previous node
        prev = head
        walker = head.next
        while walker:
            # use a temp variable to keep the b.next
            tmp = walker.next
            walker.next = prev
            if prev == head:
                prev.next = None
            prev = walker
            walker = tmp
        return prev

if __name__ == "__main__":
    head = linked_list([1,2,3,4,5])
    ret = Solution().reverseList(head)
    print_linked_list(ret)
