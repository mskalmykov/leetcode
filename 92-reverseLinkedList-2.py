from linkedlist import ListNode, linkedListFromArray
from typing import Optional

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        before = None
        after = None
        n = head
        i = 1

        while i < left:
            before = n
            n = n.next
            i += 1
        lNode = n

        prev = None
        while i < right:
            t = n.next
            n.next = prev
            prev = n

            n = t
            after = n.next
            i += 1

        n.next = prev
        lNode.next = after

        if before:
            before.next = n
        else:
            return n

        return head

print(Solution().reverseBetween(head = linkedListFromArray([3,5]), left = 1, right = 2))
print(Solution().reverseBetween(head = linkedListFromArray([3,5]), left = 1, right = 1))
print(Solution().reverseBetween(head = linkedListFromArray([1,2,3,4,5]), left = 2, right = 4))
print(Solution().reverseBetween(head = ListNode(5), left = 1, right = 1))
