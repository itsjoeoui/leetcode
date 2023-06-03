/*
 * @lc app=leetcode id=121 lang=cpp
 *
 * [121] Best Time to Buy and Sell Stock
 *
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
 *
 * algorithms
 * Easy (54.35%)
 * Likes:    25556
 * Dislikes: 804
 * Total Accepted:    3.4M
 * Total Submissions: 6.2M
 * Testcase Example:  '[7,1,5,3,6,4]'
 *
 * You are given an array prices where prices[i] is the price of a given stock
 * on the i^th day.
 *
 * You want to maximize your profit by choosing a single day to buy one stock
 * and choosing a different day in the future to sell that stock.
 *
 * Return the maximum profit you can achieve from this transaction. If you
 * cannot achieve any profit, return 0.
 *
 *
 * Example 1:
 *
 *
 * Input: prices = [7,1,5,3,6,4]
 * Output: 5
 * Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit
 * = 6-1 = 5.
 * Note that buying on day 2 and selling on day 1 is not allowed because you
 * must buy before you sell.
 *
 *
 * Example 2:
 *
 *
 * Input: prices = [7,6,4,3,1]
 * Output: 0
 * Explanation: In this case, no transactions are done and the max profit =
 * 0.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= prices.length <= 10^5
 * 0 <= prices[i] <= 10^4
 *
 *
 */

// @lc code=start
class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        // two pointers, in this case it is a sliding window
        // time complexity: O(n)
        // space complexity: O(1)
        if (prices.size() <= 1)
            return 0;
        int lp = 0;
        int rp = 1;
        int maxProfit = 0;
        while (rp < prices.size())
        {
            if (prices[lp] < prices[rp])
            {
                maxProfit = max(maxProfit, prices[rp] - prices[lp]);
            }
            else
            {
                lp = rp;
            }
            rp++;
        }
        return maxProfit;
    }
};
// @lc code=end
