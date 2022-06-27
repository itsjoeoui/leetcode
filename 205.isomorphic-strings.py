#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        history = dict()
        for i in range(len(s)):
            if not s[i] in history.keys():
                if t[i] in history.values():
                    return False
                history[s[i]] = t[i]
            else:
                if history[s[i]] != t[i]:
                    return False
        return True

# @lc code=end
