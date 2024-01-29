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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        slow = fast = head

        while fast:
            fast = fast.next
            if not fast:
                break
            else:
                fast = fast.next
                prev = slow
                slow = slow.next

        if prev:
            prev.next = slow.next
            return head
        else:
            return None
    
a = ListNode()
a.fillFromList([0,1,2,3,4])
print(a)
b = Solution().deleteMiddle(a)
print(b)
