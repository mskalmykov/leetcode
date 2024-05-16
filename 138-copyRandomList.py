from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        newList = Node(head.val)
        pNew = newList
        pOld = head
        mapOldToNew = {}

        while pOld:
            mapOldToNew[pOld] = pNew
            if pOld.next:
                pNew.next = Node(pOld.next.val)
                pNew = pNew.next
            pOld = pOld.next

        pNew = newList
        pOld = head

        while pOld:
            if pOld.random:
                pNew.random = mapOldToNew[pOld.random]
            pNew = pNew.next
            pOld = pOld.next

        return newList

