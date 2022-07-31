#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        rtn = []
        queue = deque([root])
        lToR = True

        while queue:
            level = len(queue)
            tmp = []
            for _ in range(level):
                node = queue.popleft()
                tmp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if lToR:
                rtn.append(tmp)
            else:
                rtn.append(tmp[::-1])
            lToR = not lToR

        return rtn
# @lc code=end
