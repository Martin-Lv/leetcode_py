from common import *

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(m-1):
            prev = prev.next
        start = prev.next
        then = start.next
        
        for i in range(n-m):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        return dummy.next

if __name__ == "__main__":
    head = linked_list([1,2,3,4,5])
    ret = Solution().reverseBetween(head, 2,4)
    print_linked_list(ret)

        