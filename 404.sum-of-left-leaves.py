#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Time: O(n)
        # Space: O(w)

        from collections import deque
        queue, total = deque([(root, False)]), 0

        while queue:
            node, isLeft = queue.popleft()

            if node.right is None and node.left is None and isLeft:
                total += node.val
            else:
                if node.left:
                    queue.append((node.left, True))

                if node.right:
                    queue.append((node.right, False))
        return total


# @lc code=end
