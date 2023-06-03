package leetcode

/*
 * @lc app=leetcode id=704 lang=golang
 *
 * [704] Binary Search
 */

// @lc code=start
func search(nums []int, target int) int {
	lp, rp := 0, len(nums)-1
	for lp <= rp {
		mid := lp + (rp-lp)/2
		if nums[mid] > target {
			rp = mid - 1
		} else if nums[mid] < target {
			lp = mid + 1
		} else {
			return mid
		}
	}
	return -1
}

// @lc code=end
