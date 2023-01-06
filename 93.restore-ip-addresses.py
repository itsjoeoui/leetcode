#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (43.87%)
# Likes:    3312
# Dislikes: 668
# Total Accepted:    335.5K
# Total Submissions: 764.7K
# Testcase Example:  '"25525511135"'
#
# A valid IP address consists of exactly four integers separated by single
# dots. Each integer is between 0 and 255 (inclusive) and cannot have leading
# zeros.
#
#
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but
# "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP
# addresses.
#
#
# Given a string s containing only digits, return all possible valid IP
# addresses that can be formed by inserting dots into s. You are not allowed to
# reorder or remove any digits in s. You may return the valid IP addresses in
# any order.
#
#
# Example 1:
#
#
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
#
#
# Example 2:
#
#
# Input: s = "0000"
# Output: ["0.0.0.0"]
#
#
# Example 3:
#
#
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 20
# s consists of digits only.
#
#
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return

        rtn = []
        n = len(s)

        def dfs(curPath, curIdx, curLen):
            if curIdx == n:
                if curLen == 4:
                    rtn.append(".".join(curPath[:]))
            else:
                if curLen == 4:
                    return
                if s[curIdx] == "0":
                    curPath.append(s[curIdx])
                    dfs(curPath, curIdx + 1, curLen + 1)
                    curPath.pop()
                else:
                    offset = min(n, curIdx + 3)
                    for i in range(curIdx, offset, 1):
                        if int(s[curIdx : i + 1]) <= 255:
                            curPath.append(s[curIdx : i + 1])
                            dfs(curPath, i + 1, curLen + 1)
                            curPath.pop()

        dfs([], 0, 0)
        return rtn


# @lc code=end
