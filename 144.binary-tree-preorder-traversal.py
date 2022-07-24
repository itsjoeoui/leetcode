#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        stack = deque([root])
        rtn = []
        while stack:
            node = stack.pop()
            if node:
                rtn.append(node.val)
                # First in last out, since we want left first, then append it last
                stack.append(node.right)
                stack.append(node.left)
        return rtn
# @lc code=end
