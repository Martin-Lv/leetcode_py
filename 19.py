"""
To remove the nth node from a singly-linked list, we need the node before the nth node.
1. create a node before the head, let it's next point to the head. create 2 pointer a & b pointing to the before_head.
2. let b walk n step first.
3. a & b walk at the same time, until b point to the tail.
4. now a point to the node before nth node, let it's next point to the next of next, nth node removed.
5. return the next of before_head. for the head may need to be removed.
"""

from common import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        before_head = ListNode(0)
        before_head.next = head
        a = before_head
        b = before_head
        while n > 0:
            b = b.next
            n -=1
            
        while b.next:
            a = a.next
            b = b.next
        a.next = a.next.next
        return before_head.next