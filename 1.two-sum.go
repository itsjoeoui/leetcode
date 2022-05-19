/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	history := make(map[int]int)

	for i, v := range nums {
		if idx, ok := history[target-v]; ok {
			return []int{idx, i}
		}
		history[v] = i
	}
	return nil
}

// @lc code=end

