/*
 * @lc app=leetcode id=28 lang=rust
 *
 * [28] Find the Index of the First Occurrence in a String
 *
 * https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
 *
 * algorithms
 * Easy (39.90%)
 * Likes:    4375
 * Dislikes: 229
 * Total Accepted:    1.9M
 * Total Submissions: 4.7M
 * Testcase Example:  '"sadbutsad"\n"sad"'
 *
 * Given two strings needle and haystack, return the index of the first
 * occurrence of needle in haystack, or -1 if needle is not part of
 * haystack.
 *
 *
 * Example 1:
 *
 *
 * Input: haystack = "sadbutsad", needle = "sad"
 * Output: 0
 * Explanation: "sad" occurs at index 0 and 6.
 * The first occurrence is at index 0, so we return 0.
 *
 *
 * Example 2:
 *
 *
 * Input: haystack = "leetcode", needle = "leeto"
 * Output: -1
 * Explanation: "leeto" did not occur in "leetcode", so we return -1.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= haystack.length, needle.length <= 10^4
 * haystack and needle consist of only lowercase English characters.
 *
 *
 */

struct Solution {}

// @lc code=start
impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        // haystack.find(&needle).map(|i| i as i32).unwrap_or(-1)

        let first = needle.chars().nth(0).unwrap();
        let length = needle.len();

        for (idx, val) in haystack.chars().enumerate() {
            if val == first {
                match haystack.get(idx..idx + length) {
                    Some(sliced) => {
                        if sliced == needle {
                            return idx as i32;
                        }
                    }
                    None => continue,
                }
            }
        }
        -1
    }
}
// @lc code=end
