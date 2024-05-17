from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        n = head

        while n:
            if n in seen:
                return True
            else:
                seen.add(n)
                n = n.next
        
        return False