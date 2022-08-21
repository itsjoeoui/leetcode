#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_len, l_ind, r_ind = 0, -1, -1
        for i in range(len(s)):

            left = right = i
            while left > 0:
                if s[left-1] == s[left]:
                    left = left - 1
                else:
                    break

            while right < len(s)-1:
                if s[right+1] == s[right]:
                    right = right + 1
                else:
                    break

            while True:
                if left - 1 >= 0 and right + 1 < len(s):
                    if s[left-1] == s[right+1]:
                        left = left - 1
                        right = right + 1
                    else:
                        break
                else:
                    break

            if right - left + 1 > max_len:
                max_len = right - left + 1
                l_ind, r_ind = left, right

        return s[l_ind: r_ind+1]

# @lc code=end
