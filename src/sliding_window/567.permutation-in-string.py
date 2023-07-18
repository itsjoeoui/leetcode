#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.19%)
# Likes:    10193
# Dislikes: 328
# Total Accepted:    682.2K
# Total Submissions: 1.5M
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of
# s2.
#
#
# Example 1:
#
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
#
# Example 2:
#
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = defaultdict(int)

        for i in range(len(s1)):
            count1[s1[i]] += 1

        count2 = defaultdict(int)

        for i in range(len(s1) - 1):
            count2[s2[i]] += 1

        lp = 0
        rp = len(s1) - 1

        while rp < len(s2):
            count2[s2[rp]] += 1
            rp += 1

            if count1 == count2:
                return True

            count2[s2[lp]] -= 1
            if count2[s2[lp]] == 0:
                del count2[s2[lp]]
            lp += 1
        return False


# @lc code=end
