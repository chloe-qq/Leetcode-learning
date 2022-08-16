"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Two pass solution

One pass solution by using 2 pointers with n-node separte of them
"""
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = head      
        while (first and n > 0):
            first = first.next
            n -= 1
        if (n== 0 and first == None):
            # indicating that we should move the first element
            return head.next
        second = head
        while (first):
            if (first.next==None):
                second.next = second.next.next if second.next.next is not None else None
                break
            first = first.next
            second = second.next
            
        return dummy.next
            