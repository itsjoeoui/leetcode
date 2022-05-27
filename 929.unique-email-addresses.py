#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        history = set()
        for email in emails:
            name, domain = email.split("@")
            try:
                name = name[:name.index('+')]
            except:
                pass
            finally:
                name = name.replace(".", "")
            history.add((name, domain))
        return len(history)
# @lc code=end
