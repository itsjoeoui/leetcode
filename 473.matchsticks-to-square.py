#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (40.29%)
# Likes:    3358
# Dislikes: 268
# Total Accepted:    136.7K
# Total Submissions: 339.6K
# Testcase Example:  '[1,1,2,2,2]'
#
# You are given an integer array matchsticks where matchsticks[i] is the length
# of the i^th matchstick. You want to use all the matchsticks to make one
# square. You should not break any stick, but you can link them up, and each
# matchstick must be used exactly one time.
#
# Return true if you can make this square and false otherwise.
#
#
# Example 1:
#
#
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
#
#
# Example 2:
#
#
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
#
#
#
# Constraints:
#
#
# 1 <= matchsticks.length <= 15
# 1 <= matchsticks[i] <= 10^8
#
#
#

# @lc code=start
from functools import cache


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        m = len(matchsticks)
        length = total // 4
        if length * 4 != total:
            return False

        matchsticks.sort(reverse=True)

        @cache
        def dfs(side1, side2, side3, side4, idx):
            if side1 == side2 == side3 == side4 == length:
                return True
            if idx >= m:
                return False
            cur = matchsticks[idx]
            if cur > length:
                return False
            if side1 > length or side2 > length or side3 > length or side4 > length:
                return False

            l = [side1, side2, side3, side4]
            l.sort()
            s1, s2, s3, s4 = l

            return (
                dfs(s1 + cur, s2, s3, s4, idx + 1)
                + dfs(s1, s2 + cur, s3, s4, idx + 1)
                + dfs(s1, s2, s3 + cur, s4, idx + 1)
                + dfs(s1, s2, s3, s4 + cur, idx + 1)
            )

        return dfs(0, 0, 0, 0, 0)


# @lc code=end
