package leetcode

/*
 * @lc app=leetcode id=1342 lang=golang
 *
 * [1342] Number of Steps to Reduce a Number to Zero
 */

// @lc code=start
func numberOfSteps(num int) int {
	step := 0
	for num > 0 {
		if num%2 == 0 {
			num = num / 2
		} else {
			num -= 1
		}
		step += 1
	}
	return step
}

// @lc code=end
