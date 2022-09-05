/*
 * @lc app=leetcode id=1 lang=csharp
 *
 * [1] Two Sum
 */

// @lc code=start
using System.Collections.Generic;
public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        var history = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++)
        {
            if (history.ContainsKey(target - nums[i]))
            {
                return new int[] { i, history[target - nums[i]] };
            }
            history[nums[i]] = i;
        }
        return new int[2];
    }
}
// @lc code=end

