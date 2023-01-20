#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (56.99%)
# Likes:    6976
# Dislikes: 126
# Total Accepted:    749.8K
# Total Submissions: 1.3M
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
#
#
# Example 2:
#
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
#
#

# @lc code=start
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        rtn = []

        counter = Counter(nums)

        def dfs(path, total):
            if total == l:
                rtn.append(path[:])
                return
            for n in counter:
                if counter[n]:
                    path.append(n)
                    counter[n] -= 1
                    dfs(path, total + 1)
                    path.pop()
                    counter[n] += 1

        dfs([], 0)
        return rtn


# @lc code=end
