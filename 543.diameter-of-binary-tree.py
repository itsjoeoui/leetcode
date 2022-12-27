#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def depth(root: Optional[TreeNode]) -> int:
            nonlocal ans
            if not root:
                return 0
            left: int = depth(root.left)
            right: int = depth(root.right)
            ans = max(ans, left + right)
            return max(left, right) + 1

        depth(root)

        return ans


# @lc code=end
