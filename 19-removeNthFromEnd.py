from typing import Optional
from linkedlist import ListNode, linkedListFromArray
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack =  []
        node = head
        while node:
            stack.append(node)
            node = node.next
        
        for _ in range(n):
            node = stack.pop()
            after = node.next

        if stack:
            node = stack.pop()
            node.next = after
            return head
        else:
            return after

    
print(Solution().removeNthFromEnd(linkedListFromArray([1,2,3,4,5]), 2))
print(Solution().removeNthFromEnd(linkedListFromArray([1]), 1))
print(Solution().removeNthFromEnd(linkedListFromArray([1,2]), 1))