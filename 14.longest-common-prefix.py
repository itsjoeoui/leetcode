#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_str = min(strs)
        max_str = max(strs)

        for i, c in enumerate(min_str):
            if c != max_str[i]:
                return min_str[:i]
        return min_str
# @lc code=end
