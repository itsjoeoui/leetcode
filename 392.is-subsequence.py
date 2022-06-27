#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        index = 0
        for i in t:
            if i == s[index]:
                index += 1
            if index == len(s):
                return True
        return False

# @lc code=end
