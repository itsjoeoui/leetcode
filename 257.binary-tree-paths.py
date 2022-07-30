#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        rtn = []

        def dfs(root, path):
            if root.left is None and root.right is None:
                if len(path) == 0:
                    rtn.append(str(root.val))
                else:
                    rtn.append("->".join(path)+"->"+str(root.val))
            else:
                if root.left:
                    path.append(str(root.val))
                    dfs(root.left, path)
                    path.pop()
                if root.right:
                    path.append(str(root.val))
                    dfs(root.right, path)
                    path.pop()

        dfs(root, [])
        return rtn

# @lc code=end
