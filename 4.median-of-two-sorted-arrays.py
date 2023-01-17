#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (35.59%)
# Likes:    21595
# Dislikes: 2441
# Total Accepted:    1.7M
# Total Submissions: 4.9M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            l1, l2 = l2, l1
        total = l1 + l2
        half = total // 2
        avg = (half * 2) == total

        if l1 == 0:
            if avg:
                return (nums2[half] + nums2[half - 1]) / 2
            return nums2[half]

        if nums1[-1] <= nums2[0]:
            if l1 == l2:
                return (nums1[-1] + nums2[0]) / 2
            if avg:
                return (nums2[half - l1] + nums2[half - l1 - 1]) / 2
            return nums2[half - l1]

        lp, rp = 0, l1 - 1
        while True:
            m1 = lp + (rp - lp) // 2
            m2 = half - m1 - 2

            fl = nums1[m1] if m1 >= 0 else -inf
            fr = nums1[m1 + 1] if m1 + 1 < l1 else inf
            sl = nums2[m2] if m2 >= 0 else -inf
            sr = nums2[m2 + 1] if m2 + 1 < l2 else inf

            if fl <= sr and sl <= fr:
                if avg:
                    return (max(fl, sl) + min(fr, sr)) / 2
                return min(fr, sr)

            elif fl > sr:
                rp = m1 - 1
            else:
                lp = m1 + 1


# @lc code=end
