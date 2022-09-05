#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]

        ans = []

        def dfs(start_idx, path):
            if len(path) == k:
                ans.append(path)
                return

            for i in range(start_idx, len(nums)):
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return ans


# @lc code=end
