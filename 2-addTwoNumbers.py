from typing import Optional
from linkedlist import ListNode, linkedListFromArray

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()

        pr = result
        pl1 = l1
        pl2 = l2
        s = 0

        while pl1 or pl2 or s:
            if pl1:
                s += pl1.val
                pl1 = pl1.next
            if pl2:
                s += pl2.val
                pl2 = pl2.next

            pr.val = s % 10
            s = s // 10

            if pl1 or pl2 or s:
                pr.next = ListNode()
                pr = pr.next

        return result

print(Solution().addTwoNumbers(linkedListFromArray([2,4,3]), linkedListFromArray([5,6,4])))
print(Solution().addTwoNumbers(linkedListFromArray([0]), linkedListFromArray([0])))
print(Solution().addTwoNumbers(linkedListFromArray([9,9,9,9,9,9,9]), linkedListFromArray([9,9,9,9])))