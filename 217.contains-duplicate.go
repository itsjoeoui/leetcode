/*
 * @lc app=leetcode id=217 lang=golang
 *
 * [217] Contains Duplicate
 */

// @lc code=start
func containsDuplicate(nums []int) bool {
	hm := make(map[int]bool)
	for _, v := range nums {
		if hm[v] {
			return true
		}
		hm[v] = true
	}
	return false
}

// @lc code=end

