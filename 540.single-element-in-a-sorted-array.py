#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def toLeft(idx: int) -> bool:
            # Small trick here.
            if idx % 2 == 1:
                return nums[idx] != nums[idx-1]
            else:
                '''
                It's safe to use idx-1 because if the single element is at 
                idx 0, the algo will compare idx 0 and -1.
                Then we have two cases to consider:
                Case 1: len(nums) = 1:
                In this case, toLeft returns True, r becomes -1, 
                returns nums[-1], good!
                Case 2: len(nums) > 1:
                In this case, toLeft returns False. l becomes 1, 
                then nums[0] gets returned, also good!
                '''
                return nums[idx] == nums[idx-1]

        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l) // 2
            if toLeft(m):
                r = m - 1
            else:
                l = m + 1
        return nums[r]
# @lc code=end
