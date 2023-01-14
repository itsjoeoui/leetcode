#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (44.82%)
# Likes:    5735
# Dislikes: 495
# Total Accepted:    499.2K
# Total Submissions: 1.1M
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a string s and a dictionary of strings wordDict, add spaces in s to
# construct a sentence where each word is a valid dictionary word. Return all
# such possible sentences in any order.
#
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
#
#
# Example 1:
#
#
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
#
#
# Example 2:
#
#
# Input: s = "pineapplepenapple", wordDict =
# ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
#
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        a = len(s)
        out = []
        memo = [False] * (a + 1)

        def dfs(tmp, idx):
            if memo[idx]:
                return
            if idx == a:
                out.append(" ".join(tmp))
                return

            bad = True
            for w in wordDict:
                if s[idx:].startswith(w):
                    bad = False
                    tmp.append(w)
                    dfs(tmp, idx + len(w))
                    tmp.pop()
            memo[idx] = bad

        dfs([], 0)
        return out


# @lc code=end
