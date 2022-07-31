#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Time: O(n)
        # Space: O(w)
        queue = deque([(root, "")])
        rtn = 0

        while queue:
            node, path = queue.popleft()

            if node.left is None and node.right is None:
                rtn += int(path+str(node.val))

            if node.left is not None:
                queue.append((node.left, path+str(node.val)))
            if node.right is not None:
                queue.append((node.right, path+str(node.val)))

        return rtn
# @lc code=end
