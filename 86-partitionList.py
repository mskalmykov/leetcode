from typing import Optional
from linkedlist import ListNode, linkedListFromArray

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ltNodes = ListNode()
        geNodes = ListNode()
        lt = ltNodes
        ge = geNodes

        n = head

        while n:
            if n.val < x:
                lt.next = n
                n = n.next
                lt = lt.next
                lt.next = None
            else:
                ge.next = n
                n = n.next
                ge = ge.next
                ge.next = None

        if ltNodes.next:
            lt.next = geNodes.next
            return ltNodes.next
        else:
            return geNodes.next


print(Solution().partition(linkedListFromArray([1,4,3,2,5,2]), 3))
print(Solution().partition(linkedListFromArray([2,1]), 2))