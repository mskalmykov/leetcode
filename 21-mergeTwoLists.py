from typing import Optional
from linkedlist import ListNode, linkedListFromArray

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        l1, l2 = list1, list2
        head = ListNode()
        n = head

        while l1 and l2:
            if l1.val < l2.val:
                n.next = l1
                n = n.next
                l1 = l1.next
            else:
                n.next = l2
                n = n.next
                l2 = l2.next

        if l1:
            n.next = l1
        elif l2:
            n.next = l2

        return head.next

list1 = linkedListFromArray([1,2,4])
list2 = linkedListFromArray([1,3,4])
print(Solution().mergeTwoLists(list1, list2))

list1 = linkedListFromArray([])
list2 = linkedListFromArray([])
print(Solution().mergeTwoLists(list1, list2))

list1 = linkedListFromArray([])
list2 = linkedListFromArray([0])
print(Solution().mergeTwoLists(list1, list2))
