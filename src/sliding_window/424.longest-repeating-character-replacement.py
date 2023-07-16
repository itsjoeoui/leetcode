#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (52.26%)
# Likes:    8762
# Dislikes: 373
# Total Accepted:    491.2K
# Total Submissions: 939.9K
# Testcase Example:  '"ABAB"\n2'
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
#
#
# Example 1:
#
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#
#
# Example 2:
#
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achive this answer too.
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
#
#
#

from collections import defaultdict


# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        lp = 0
        rtn = 0

        for rp in range(len(s)):
            freq[s[rp]] += 1
            most = max(freq.values())
            cost = rp - lp + 1 - most

            if cost > k:
                freq[s[lp]] -= 1
                lp += 1
            else:
                rtn = max(rtn, rp - lp + 1)

        return rtn


# @lc code=end
