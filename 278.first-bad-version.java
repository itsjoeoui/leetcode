/*
 * @lc app=leetcode id=278 lang=java
 *
 * [278] First Bad Version
 */

// @lc code=start
/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int lp = 0;
        int rp = n;
        int rtn = -1;

        while(lp <= rp) {
            n = lp + (rp - lp) / 2;
            if (isBadVersion(n)) {
                rtn = n;
                rp = n - 1;
            } else {
                lp = n + 1;
            }
        }
        return rtn;
    }
}
// @lc code=end

