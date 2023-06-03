/*
 * @lc app=leetcode id=42 lang=c
 *
 * [42] Trapping Rain Water
 *
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (58.98%)
 * Likes:    26686
 * Dislikes: 366
 * Total Accepted:    1.5M
 * Total Submissions: 2.6M
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it can trap after raining.
 *
 *
 * Example 1:
 *
 *
 * Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 * Explanation: The above elevation map (black section) is represented by array
 * [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
 * section) are being trapped.
 *
 *
 * Example 2:
 *
 *
 * Input: height = [4,2,0,3,2,5]
 * Output: 9
 *
 *
 *
 * Constraints:
 *
 *
 * n == height.length
 * 1 <= n <= 2 * 10^4
 * 0 <= height[i] <= 10^5
 *
 *
 */

// @lc code=start
int trap(int *height, int heightSize)
{
    int lp = 0;
    int rp = heightSize - 1;
    int lmax = 0;
    int rmax = 0;
    int ans = 0;
    while (lp < rp)
    {
        if (height[lp] < height[rp])
        {
            if (height[lp] >= lmax)
            {
                lmax = height[lp];
            }
            else
            {
                ans += lmax - height[lp];
            }
            lp++;
        }
        else
        {
            if (height[rp] >= rmax)
            {
                rmax = height[rp];
            }
            else
            {
                ans += rmax - height[rp];
            }
            rp--;
        }
    }
    return ans;
}
// @lc code=end
