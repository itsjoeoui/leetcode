#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (21.95%)
# Likes:    3200
# Dislikes: 389
# Total Accepted:    316.6K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane, return the maximum number of points that lie on the same straight
# line.
#
#
# Example 1:
#
#
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
#
#
# Example 2:
#
#
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 300
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# All the points are unique.
#
#
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points.sort()
        m = 0

        for i, (x1, y1) in enumerate(points):
            slopes = defaultdict(int)
            for x2, y2 in points[i + 1 :]:
                dx, dy = x2 - x1, y2 - y1
                g = gcd(dx, dy)
                k = (dx // g, dy // g)
                slopes[k] += 1
                if slopes[k] > m:
                    m = slopes[k]
        return m + 1


# @lc code=end
