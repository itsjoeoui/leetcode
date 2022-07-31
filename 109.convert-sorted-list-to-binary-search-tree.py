#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Time: O(n)
        # Space: O(log n), because the depth of the sortedListToBST recursion take log n space

        if not head:
            return

        if not head.next:
            return TreeNode(val=head.val)

        # This base case is important such that slow won't overshoot
        # If we start both slow and fast pointer at head it would not work
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid = slow.next
        slow.next = None  # Cut the linked list into two pieces

        node = TreeNode(val=mid.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)

        return node
# @lc code=end
