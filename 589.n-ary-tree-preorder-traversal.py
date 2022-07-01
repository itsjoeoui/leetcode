#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, result = [root], []
        while len(stack):
            curr = stack.pop()
            result.append(curr.val)
            stack.extend(reversed(curr.children))
        return result
# @lc code=end
