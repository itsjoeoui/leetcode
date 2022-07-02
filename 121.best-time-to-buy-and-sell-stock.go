/*
 * @lc app=leetcode id=121 lang=golang
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
func maxProfit(prices []int) int {
	// If there is only one item then just return 0
	if len(prices) <= 1 {
		return 0
	}

	base := 0 // Baseline
	// Assume the array is like [1, 5, 3]
	// Then the base will be [0, 4, 2]

	profit := 0 // Current max profit

	for i := 1; i < len(prices); i++ {
		growth := base + prices[i] - prices[i-1]
		profit = max(profit, growth)

		if growth > 0 {
			base = growth
		} else {
			// Reset the base since there is a new minimum
			base = 0
		}
	}

	return profit
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

