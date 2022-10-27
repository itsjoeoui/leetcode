#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 0
        length = len(nums)
        while fast < length:
            if nums[fast] <= nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1 
# @lc code=end

