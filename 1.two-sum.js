/*
 * @lc app=leetcode id=1 lang=javascript
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    let history = {};
    for (let i = 0; i < nums.length; i++) {
        let currentNum = nums[i];
        let currentTarget = target - currentNum;
        if (currentTarget in history) {
            return [history[currentTarget], i];
        } else {
            history[currentNum] = i;
        }
    }
};
// @lc code=end

