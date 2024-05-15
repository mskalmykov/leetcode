from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        elements = []
        node = self

        while node:
            elements.append(node.val)
            node = node.next

        return str(elements)
    
def linkedListFromArray(vals: List) -> ListNode:
    if not vals:
        return None
    
    root = ListNode(vals[0])
    n = root

    for elem in vals[1:]:
        n.next = ListNode(elem)
        n = n.next

    return root