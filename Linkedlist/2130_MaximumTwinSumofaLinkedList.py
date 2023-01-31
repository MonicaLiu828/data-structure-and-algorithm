# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # use fast, slow to find the half of this linkedlist
        fast = head
        slow = head
        lastSec = None
        while fast:
            slow = slow.next
            lastSec = fast
            fast = fast.next.next

        # reverse last half of linkedlist -> (1,2,3,4) -> (1,2)(4,3)
        def reverseNode(pos):
            prev = None
            while pos:
                nextNode = pos.next
                pos.next = prev
                prev = pos
                pos = nextNode
            return prev

        newHalf = reverseNode(slow)
        # let leftstart and rightstart to start from each half of list and find the total max sum
        sum = 0
        leftstart = head
        rightstart = newHalf
        while rightstart:
            sum = max(sum, leftstart.val + rightstart.val)
            rightstart = rightstart.next
            leftstart = leftstart.next
        return sum

