#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(options, total, path, rtn=[]):
            if total == 0:
                rtn.append(path)
                return

            for i in range(len(options)):
                tmp = options[i]
                if tmp > total:
                    break
                dfs(options[i:], total - options[i], path + [options[i]], rtn)
            return rtn

        return dfs(sorted(candidates), target, [])
# @lc code=end
