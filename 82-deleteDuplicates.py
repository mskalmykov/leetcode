from linkedlist import ListNode, linkedListFromArray
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        newHead = None
        lastOkNode = None
        prevNode = head
        n = head.next
        curCount = 1

        while n:
            if n.val == prevNode.val:
                curCount += 1
            else:
                if curCount == 1:
                    if not newHead:
                        newHead = prevNode
                    if lastOkNode:
                        lastOkNode.next = prevNode
                    lastOkNode = prevNode
                    lastOkNode.next = None
                else:
                    curCount = 1

            prevNode = n
            n = n.next

        if curCount == 1:
            if not newHead:
                newHead = prevNode
            if lastOkNode:
                lastOkNode.next = prevNode

        return newHead

print(Solution().deleteDuplicates(linkedListFromArray([1,2,3,3,4,4,5])))
print(Solution().deleteDuplicates(linkedListFromArray([1,1,1,2,3])))