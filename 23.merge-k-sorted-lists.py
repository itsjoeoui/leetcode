#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        heap = []
        head = cur = ListNode()

        for node in lists:
            if node:
                heappush(heap, node)

        while heap:
            node = heappop(heap)
            cur.next = ListNode(node.val)
            cur = cur.next
            node = node.next
            if node:
                heappush(heap, node)

        return head.next

# @lc code=end
