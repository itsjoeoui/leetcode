#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
#
# algorithms
# Medium (57.24%)
# Likes:    2589
# Dislikes: 188
# Total Accepted:    116K
# Total Submissions: 202.7K
# Testcase Example:  '3\n7'
#
# Given two integers n and k, return an array of all the integers of length n
# where the difference between every two consecutive digits is k. You may
# return the answer in any order.
#
# Note that the integers should not have leading zeros. Integers as 02 and 043
# are not allowed.
#
#
# Example 1:
#
#
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading
# zeroes.
#
#
# Example 2:
#
#
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
#
#
#
# Constraints:
#
#
# 2 <= n <= 9
# 0 <= k <= 9
#
#
#

# @lc code=start
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        out = []

        def dfs(tmp):
            if len(tmp) == n:
                out.append(int("".join(map(str, tmp))))
                return

            last = tmp[-1]
            for i in set([last + k, last - k]):
                if 0 <= i < 10:
                    tmp.append(i)
                    dfs(tmp)
                    tmp.pop()

        for i in range(1, 10):
            dfs([i])

        return out


# @lc code=end
