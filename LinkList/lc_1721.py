# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
# swap values rather than node
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pre = ListNode()
        pre.next = head
        first = head

        while (first and k > 1):
            first = first.next
            k -= 1
        second = head
        cur = first
        first_val = first.val
        while (first):
            if (first.next == None):
                second_val = second.val
                second.val = first_val
                cur.val = second_val
            first = first.next
            second = second.next
        return pre.next
                