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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        evenStart = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenStart

        return head
    
a = ListNode()
a.fillFromList([1,2,3,4,5,6])
print(a)
b = Solution().oddEvenList(a)
print(b)
