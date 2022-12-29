#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        for _ in range(k - 1):
            root = self.deleteNode(root, self.getSmallest(root))
        return self.getSmallest(root)

    def getSmallest(self, root: Optional[TreeNode]) -> int:
        while (root.left):
            root = root.left
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return None
            root.val = self.getSmallest(root.right)
            root.right = self.deleteNode(root.right, root.val)

        return root


# @lc code=end
