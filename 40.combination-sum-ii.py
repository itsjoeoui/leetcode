#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time: O(2^n) since there are 2^n combinations in total
        # Or we can think of it as each step we have 2 options, pick the number or not
        # Space: O(n), the stack will have maximum n numbers in it

        def dfs(start, total, path, rtn=[]):
            if total == 0:
                rtn.append(path)
                return

            for i in range(start, len(candidates)):
                tmp = candidates[i]

                # Very important here! We don't use `i > 0` because we always want to count the
                # first element in this recursive step even if it is the same as one before.
                # To avoid over-counting, we just ignore the duplicates after the first element.

                '''
                Example, if my upcoming options array is like [1,1,1,2,3]
                It is okay if I choose whatever path + array[0]
                However, once we go pass the first index, we don't want any
                duplications, for example, path + array[1] or path + array[2] 
                would be examples of repeated numbers.
                '''

                if i > start and tmp == candidates[i-1]:
                    continue

                if tmp > total:  # Already too big so just break
                    break

                dfs(i+1, total - tmp, path + [tmp], rtn)
            return rtn

        candidates.sort()

        return dfs(0, target, [])
# @lc code=end
