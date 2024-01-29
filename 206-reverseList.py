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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        center = head

        while center:
            right = center.next
            center.next = left
            left = center
            center = right

        return left
        

a = ListNode()
a.fillFromList([10,20,30,40,50])
print(a)
b = Solution().reverseList(a)
print(b)
