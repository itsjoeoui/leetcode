#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = [root]
        result = []
        while level:
            result.append([n.val for n in level])
            # temp = []
            # for n in level:
            #     temp.append(n.left)
            #     temp.append(n.right)
            # level = [i for i in temp if i]
            level = [child for n in level for child in (
                n.left, n.right) if child]
        return result
# @lc code=end
