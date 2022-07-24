#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        from collections import deque
        queue = deque([root.left, root.right])

        while queue:
            left, right = queue.popleft(), queue.popleft()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            # Append does not work here, it will append the list into the list
            # queue.append([left.right, right.left, left.left, right.right])
            # Therefore, use += or queue.extend()
            queue += [left.right, right.left, left.left, right.right]
        return True
# @lc code=end
