/*
 * @lc app=leetcode id=1689 lang=golang
 *
 * [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
 */

// @lc code=start
func minPartitions(n string) int {
	// Both result and v will be rune type
	result := '0'
	// fmt.Printf("%v", '0') => 48
	// fmt.Printf("%v", '1') => 49
	for _, v := range n {
		// Since v is also rune type, we can directly compare them
		if v > result {
			result = v
		}
	}
	// Convert rune back to an integer
	// For example, if result is '1', which represents 49 in rune,
	// then '1' - '0' is essentially 49 - 48, which will be 1
	return int(result - '0')
}

// @lc code=end

