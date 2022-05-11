#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        history = dict()
        start = 0
        length = 0
        longest = 0

        for i, v in enumerate(s):
            if v not in history:
                length += 1
            else:
                if length > longest:
                    longest = length
                start = max(history[v] + 1, start)
                length = i-start+1
            history[v] = i

        return max(longest, length)
# @lc code=end
