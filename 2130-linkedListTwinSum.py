from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = '[' + str(self.val)
        n = self.next
        while n != None:
            s += ',' + str(n.val)
            n = n.next
        s += ']'

        return s
    
    def fillFromList(self, values: List[int]):
        if not values:
            return
        obj = self
        obj.val = values[0]
        for v in values[1:]:
            obj.next = ListNode()
            obj = obj.next
            obj.val = v

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseList(l: ListNode) -> ListNode:
            left = None
            center = l

            while center:
                right = center.next
                center.next = left
                left = center
                center = right
            
            return left

        slow = fast = head

        while fast:
            fast = fast.next.next
            slow = slow.next

        listA = head
        listB = reverseList(slow)
        lastEl = listB
        maxSum = float('-inf')

        while listB:
            maxSum = max(maxSum, listA.val + listB.val)
            listA = listA.next
            listB = listB.next

        reverseList(lastEl)

        return maxSum
                
    
a = ListNode()
a.fillFromList([1,2])
print(a)
print(Solution().pairSum(a))
print(a)
