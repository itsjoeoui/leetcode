#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        tracker = defaultdict(int)
        rtn = 0
        for rp in range(len(s)):
            tracker[s[rp]] += 1
            while tracker[s[rp]] > 1:
                tracker[s[lp]] -= 1
                lp += 1
            rtn = max(rtn, rp - lp + 1)
        return rtn


# @lc code=end
