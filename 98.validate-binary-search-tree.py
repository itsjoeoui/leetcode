#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, max_val, min_val):
            if node is None:
                return True
            if min_val < node.val < max_val:
                return dfs(node.left, node.val, min_val) and dfs(node.right, max_val, node.val)
            return False
        return dfs(root.left, root.val, -float('inf')) and dfs(root.right, float('inf'), root.val)
# @lc code=end
