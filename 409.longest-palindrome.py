#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = set()
        for letter in s:
            if letter not in odds:
                odds.add(letter)
            else:
                odds.remove(letter)
        return len(s) - len(odds) + bool(odds)
# @lc code=end
