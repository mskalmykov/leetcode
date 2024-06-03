from typing import Optional
from linkedlist import ListNode, linkedListFromArray

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head

        n = head
        cnt = 1

        while n != None and cnt < k:
            n = n.next
            cnt += 1
        
        if cnt != k or n == None: return head

        newHead = n
        tail = n.next
        
        cnt = 1
        prev = head
        n = head.next

        while n != None and cnt < k:
            oldNext = n.next
            n.next = prev
            prev = n
            n = oldNext
            cnt += 1
        
        if tail:
            head.next = self.reverseKGroup(tail, k)
        else:
            head.next = None

        return newHead

print(Solution().reverseKGroup(linkedListFromArray([1,2,3,4,5]), 2))
print(Solution().reverseKGroup(linkedListFromArray([1,2,3,4,5]), 3))
print(Solution().reverseKGroup(linkedListFromArray([1,2,3,4,5]), 5))
print(Solution().reverseKGroup(linkedListFromArray([1,2,3,4,5]), 6))
