#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp: int = 0
        rp: int = len(s) - 1
        while (lp <rp):
            if not (s[lp].isalnum()):
                lp += 1
            elif not (s[rp].isalnum()):
                rp -= 1
            else:
                if (s[lp].lower() != s[rp].lower()):
                    return False
                lp += 1
                rp -= 1
            
        return True

        # @lc code=end
