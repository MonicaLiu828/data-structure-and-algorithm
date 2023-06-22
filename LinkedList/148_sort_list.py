# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #  get the mid of the linkedlist and split the whole list into two parts
        #  sort the left part
        #  sort the right part
        #  use merget sort to link these two parts
        if not head or not head.next:
            return head

        def findMid(list: [ListNode]) -> ListNode:
            if not list or not list.next:
                return list
            slowPos = list
            quickPos = list
            while slowPos and slowPos.next and quickPos and quickPos.next and quickPos.next.next:
                slowPos = slowPos.next
                quickPos = quickPos.next.next
            return slowPos

        def merge_half(left: [ListNode], right: [ListNode]) -> [ListNode]:
            if not left:
                return right
            if not right:
                return left
            dummy = ListNode(-1)
            pos = dummy
            while left and right:
                if left.val < right.val:
                    pos.next = left
                    pos = pos.next
                    left = left.next
                else:
                    pos.next = right
                    pos = pos.next
                    right = right.next

            if left:
                pos.next = left
            else:
                pos.next = right

            return dummy.next

        mid = findMid(head)
        print(mid)
        right = mid.next
        mid.next = None
        left = head

        sorted_left = self.sortList(left)
        sorted_right = self.sortList(right)
        # print(sorted_left, sorted_right)
        return merge_half(sorted_left, sorted_right)

        #  时间复杂度nlogn, 空间复杂度 都是O(1) 的。 由于链表的归并排序不用创建一个长度为N的list














