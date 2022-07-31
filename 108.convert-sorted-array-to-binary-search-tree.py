#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Time: O(n)
        # Space: O(log n)

        def buildTree(lower, upper):
            if lower > upper:
                return None

            mid = lower + (upper - lower) // 2

#             node = TreeNode(val = nums[mid])
#             node.left = buildTree(lower, mid-1)
#             node.right = buildTree(mid + 1, upper)
#             return node

            return TreeNode(nums[mid], buildTree(lower, mid-1), buildTree(mid + 1, upper))

        return buildTree(0, len(nums)-1)

# @lc code=end
