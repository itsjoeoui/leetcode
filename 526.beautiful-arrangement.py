#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (64.52%)
# Likes:    2672
# Dislikes: 329
# Total Accepted:    146.7K
# Total Submissions: 227.5K
# Testcase Example:  '2'
#
# Suppose you have n integers labeled 1 through n. A permutation of those n
# integers perm (1-indexed) is considered a beautiful arrangement if for every
# i (1 <= i <= n), either of the following is true:
#
#
# perm[i] is divisible by i.
# i is divisible by perm[i].
#
#
# Given an integer n, return the number of the beautiful arrangements that you
# can construct.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation:
# The first beautiful arrangement is [1,2]:
# ⁠   - perm[1] = 1 is divisible by i = 1
# ⁠   - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
# ⁠   - perm[1] = 2 is divisible by i = 1
# ⁠   - i = 2 is divisible by perm[2] = 1
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 15
#
#
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        seen = [False] * (n + 1)

        def dfs(cur: int) -> int:
            if cur == n + 1:
                return 1

            count = 0
            for i in range(1, n + 1):
                if (not seen[i]) and (cur % i == 0 or i % cur == 0):
                    seen[i] = True
                    count += dfs(cur + 1)
                    seen[i] = False

            return count

        return dfs(1)


# @lc code=end
