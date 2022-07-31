#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(w)
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:

            level = len(queue)
            tmp = []
            for _ in range(level):

                n = queue.popleft()
                tmp.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            result.append(tmp)

        return result[::-1]
# @lc code=end
