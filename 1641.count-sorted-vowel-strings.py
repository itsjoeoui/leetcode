#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#

# @lc code=start
class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5

        def gen_multiplier(n):
            if n == 2:
                return [1, 1, 1, 1, 1]
            my_arr = gen_multiplier(n-1)
            return [sum(my_arr[:i+1]) for i in range(len(my_arr))]

        multi = gen_multiplier(n)
        return sum([v*(5-i) for i, v in enumerate(multi)])
# @lc code=end
