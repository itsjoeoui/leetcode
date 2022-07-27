#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        from collections import deque
        queue = deque([root])

        while len(queue) > 0:
            node = queue.popleft()
            if node.left is None and node.right is None:
                if node.val == targetSum:
                    return True
            if node.left:
                node.left.val += node.val
                queue.append(node.left)
            if node.right:
                node.right.val += node.val
                queue.append(node.right)

        return False
# @lc code=end
