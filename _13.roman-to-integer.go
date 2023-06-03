package leetcode

/*
 * @lc app=leetcode id=13 lang=golang
 *
 * [13] Roman to Integer
 */

// @lc code=start
func romanToInt(s string) int {
	rtoi := map[uint8]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	lastVal := rtoi[uint8(s[0])]
	total := lastVal

	var currentVal int

	for i := 1; i < len(s); i++ {
		currentVal = rtoi[uint8(s[i])]
		if lastVal < currentVal {
			total -= lastVal * 2
		}

		total += currentVal
		lastVal = currentVal
	}
	return total
}

// @lc code=end
