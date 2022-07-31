#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Time: O(n)
        # Space: O(log n)

        res = []

        def dfs(add, close, path):

            if close == 0:
                res.append(path)

            if add > 0:
                dfs(add-1, close, path+"(")
            if close > add:
                dfs(add, close-1, path+")")

        dfs(n-1, n, "(")
        return res
# @lc code=end
