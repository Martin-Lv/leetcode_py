from common import *

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = 0
        pwalker = ListNode(0)
        pres = pwalker
        while l1 or l2 or tmp > 0:
            if not pwalker.next:
                pwalker.next = ListNode(0)
            sum = tmp
            tmp = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum >= 10:
                sum -= 10
                tmp = 1
            pwalker.next.val = sum
            pwalker = pwalker.next
        return pres.next
