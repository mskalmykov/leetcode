from linkedlist import ListNode, linkedListFromArray
from typing import Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        l = 1
        n = head

        while n.next:       # determine the length of the list
            n = n.next
            l += 1
        
        k = k % l           # number of shift steps
        if k == 0:
            return head
        else:
            n.next = head

        n = head
        i = 1
        while i < l - k:    # find the last node of rotated list
            n = n.next
            i += 1
        
        newHead = n.next    # the next node will be the head of new list
        n.next = None

        return newHead

print(Solution().rotateRight(head = linkedListFromArray([1,2,3,4,5]), k = 2))
print(Solution().rotateRight(head = linkedListFromArray([0,1,2]), k = 4))