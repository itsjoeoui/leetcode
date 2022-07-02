/*
 * @lc app=leetcode id=278 lang=golang
 *
 * [278] First Bad Version
 */

// @lc code=start
/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func firstBadVersion(n int) int {
	lp, rp := 1, n
	for lp <= rp {
		mid := lp + (rp-lp)/2
		if isBadVersion(mid) {
			rp = mid - 1
		} else {
			lp = mid + 1
		}
	}
	return lp
}

// @lc code=end

