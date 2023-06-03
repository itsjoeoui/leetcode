package leetcode

/*
 * @lc app=leetcode id=367 lang=golang
 *
 * [367] Valid Perfect Square
 */

// @lc code=start
func isPerfectSquare(num int) bool {
	for i := 0; i < num/2+2; i++ {
		if i*i == num {
			return true
		}
		if i*i > num {
			break
		}
	}
	return false
}

// @lc code=end
