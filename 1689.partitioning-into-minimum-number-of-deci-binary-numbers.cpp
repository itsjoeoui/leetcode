/*
 * @lc app=leetcode id=1689 lang=cpp
 *
 * [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
 */

// @lc code=start
class Solution
{
public:
    int minPartitions(string n)
    {
        char result = '0';
        for (char digit : n)
        {
            result = max(result, digit);
        }
        return result - '0';
    }
};
// @lc code=end
