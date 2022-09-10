/*
 * @lc app=leetcode id=55 lang=golang
 *
 * [55] Jump Game
 */

// @lc code=start
func canJump(nums []int) bool {
	memo := make(map[int]bool)
	return dfs(&nums, 0, &memo)
}

func dfs(nums *[]int, curIdx int, memo *map[int]bool) bool {
	if curIdx >= len(*nums)-1 {
		return true
	}

	if val, ok := (*memo)[curIdx]; ok {
		return val
	}

	if (*nums)[curIdx] == 0 {
		(*memo)[curIdx] = false
		return false
	}

	status := false
	for i := (*nums)[curIdx]; i >= 1; i-- {
		if curIdx+i <= len(*nums) {
			if dfs(nums, curIdx+i, memo) {
				status = true
				break
			}
		}
	}

	(*memo)[curIdx] = status
	return status
}

// @lc code=end

