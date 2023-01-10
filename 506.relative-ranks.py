#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#
# https://leetcode.com/problems/relative-ranks/description/
#
# algorithms
# Easy (59.57%)
# Likes:    867
# Dislikes: 43
# Total Accepted:    113.3K
# Total Submissions: 189.9K
# Testcase Example:  '[5,4,3,2,1]'
#
# You are given an integer array score of size n, where score[i] is the score
# of the i^th athlete in a competition. All the scores are guaranteed to be
# unique.
#
# The athletes are placed based on their scores, where the 1^st place athlete
# has the highest score, the 2^nd place athlete has the 2^nd highest score, and
# so on. The placement of each athlete determines their rank:
#
#
# The 1^st place athlete's rank is "Gold Medal".
# The 2^nd place athlete's rank is "Silver Medal".
# The 3^rd place athlete's rank is "Bronze Medal".
# For the 4^th place to the n^th place athlete, their rank is their placement
# number (i.e., the x^th place athlete's rank is "x").
#
#
# Return an array answer of size n where answer[i] is the rank of the i^th
# athlete.
#
#
# Example 1:
#
#
# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1^st, 2^nd, 3^rd, 4^th, 5^th].
#
# Example 2:
#
#
# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1^st, 5^th, 3^rd, 2^nd, 4^th].
#
#
#
#
# Constraints:
#
#
# n == score.length
# 1 <= n <= 10^4
# 0 <= score[i] <= 10^6
# All the values in score are unique.
#
#
#

# @lc code=start
from heapq import heappop, heappush


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        ranks = []
        for i, v in enumerate(score):
            heappush(ranks, (-v, i))

        for i in range(len(score)):
            _, idx = heappop(ranks)
            match i:
                case 0:
                    score[idx] = "Gold Medal"
                    continue
                case 1:
                    score[idx] = "Silver Medal"
                    continue
                case 2:
                    score[idx] = "Bronze Medal"
                    continue
                case default:
                    score[idx] = str(i + 1)
        return score


# @lc code=end
