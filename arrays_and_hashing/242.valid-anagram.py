#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        from collections import defaultdict

        track: defaultdict = defaultdict(lambda: 0)
        for i in range(len(s)):
            track[s[i]] += 1
            track[t[i]] -= 1

        for v in track.values():
            if v != 0:
                return False
        return True


# @lc code=end
