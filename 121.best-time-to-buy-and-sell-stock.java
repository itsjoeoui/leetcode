/*
 * @lc app=leetcode id=121 lang=java
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices) {
        int slow = 0;
        int fast = 1;
        int rtn = 0;

        while (fast < prices.length) {
            int cur = prices[fast] - prices[slow];
            if (cur < 0) {
                slow = fast;
                fast = slow + 1;
            } else {
                rtn = Math.max(rtn, cur);
                fast++;
            }
        }
        return rtn;
    }
}
// @lc code=end
