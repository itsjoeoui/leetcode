#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = dummy = ListNode()  # Both var refers to the same ListNode object
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                # Moving the pointer forward by one
                # This does not modify the underlying object
                list1, dummy = list1.next, dummy.next
            else:
                dummy.next = list2
                list2, dummy = list2.next, dummy.next
        if list1 or list2:
            dummy.next = list1 if list1 else list2
        return result.next
# @lc code=end
