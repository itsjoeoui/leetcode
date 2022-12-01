#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapify(nums)
        for _ in range(k-1):
            rtn = heappop(nums)
        return -nums[0]

# @lc code=end
