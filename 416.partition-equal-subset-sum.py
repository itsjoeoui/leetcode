#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total: int = sum(nums)
        if total % 2 == 1:
            return False
        half: int = total // 2

        memo: list[bool] = [True] + [False] * half
        for n in nums:
            for i in range(half, n - 1, -1):
                memo[i] |= memo[i-n]
        return memo[half]

# @lc code=end
