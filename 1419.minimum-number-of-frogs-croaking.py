#
# @lc app=leetcode id=1419 lang=python3
#
# [1419] Minimum Number of Frogs Croaking
#

# @lc code=start
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c, r, o, a, k = 0, 0, 0, 0, 0
        amount = 0
        for letter in croakOfFrogs:
            if letter == 'c':
                c += 1
                amount = max(amount, c-k)
            elif letter == 'r':
                if r < c:
                    r += 1
                else:
                    return -1
            elif letter == 'o':
                if o < r:
                    o += 1
                else:
                    return -1
            elif letter == 'a':
                if a < o:
                    a += 1
                else:
                    return -1
            else:
                if k < a:
                    k += 1
                else:
                    return -1

        return amount if c == k else -1

# @lc code=end
