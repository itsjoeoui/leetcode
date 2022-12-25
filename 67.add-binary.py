#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aidx = len(a) - 1
        bidx = len(b) - 1
        carry = 0
        sum = ""

        while aidx >= 0 or bidx >= 0 or carry:
            if aidx >= 0:
                carry += int(a[aidx])
            if bidx >= 0:
                carry += int(b[bidx])

            sum = str(carry % 2) + sum
            carry //= 2

            aidx -= 1
            bidx -= 1
        return sum
# @lc code=end
