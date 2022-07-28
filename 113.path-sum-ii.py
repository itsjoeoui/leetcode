#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        queue = deque([(root, root.val, [root.val])])
        res = []

        while queue:
            node, total, path = queue.popleft()
            if not node.left and not node.right and total == targetSum:
                res.append(path)
            if node.left:
                queue.append(
                    (node.left, total+node.left.val, path+[node.left.val]))
            if node.right:
                queue.append(
                    (node.right, total+node.right.val, path+[node.right.val]))

        return res
# @lc code=end
