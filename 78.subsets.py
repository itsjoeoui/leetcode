#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from tracemalloc import start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(start_idx, path):
            if start_idx == len(nums):
                ans.append(path)
                return

            dfs(start_idx+1, path + [nums[start_idx]])
            dfs(start_idx+1, path)
        dfs(0, [])

        return ans
# @lc code=end
