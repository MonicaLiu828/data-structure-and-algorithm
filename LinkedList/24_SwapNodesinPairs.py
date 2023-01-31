
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = null
        # curr = head
        # next_node = curr.next
        # curr.next = prev
        # prev.
        if not head:
            return None
        if not head.next:
            return head
        # if not head.next.next:
        #     head.next.next = head
        #     start = head.next
        #     head.next = None
        #     return start
        newStart = head.next.next
        # head.next.next = None
        swaped = self.swapPairs(newStart)
        next_node = head.next
        next_node.next = head
        head.next=swaped
        return next_node

solution2:


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return from here
        if not head or not head.next:
            return head
        dummy = head.next
        prev = None
        curr = head
        while curr and curr.next:
            if not prev:
                prev = head
            elif prev:
                prev.next = curr.next

            nextNode = curr.next.next
            curr.next.next = curr
            prev = curr
            curr.next = nextNode
            curr = nextNode
        return dummy