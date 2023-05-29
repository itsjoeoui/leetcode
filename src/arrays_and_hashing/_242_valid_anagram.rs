/*
 * @lc app=leetcode id=242 lang=rust
 *
 * [242] Valid Anagram
 *
 * https://leetcode.com/problems/valid-anagram/description/
 *
 * algorithms
 * Easy (62.87%)
 * Likes:    9147
 * Dislikes: 286
 * Total Accepted:    2.2M
 * Total Submissions: 3.5M
 * Testcase Example:  '"anagram"\n"nagaram"'
 *
 * Given two strings s and t, return true if t is an anagram of s, and false
 * otherwise.
 *
 * An Anagram is a word or phrase formed by rearranging the letters of a
 * different word or phrase, typically using all the original letters exactly
 * once.
 *
 *
 * Example 1:
 * Input: s = "anagram", t = "nagaram"
 * Output: true
 * Example 2:
 * Input: s = "rat", t = "car"
 * Output: false
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length, t.length <= 5 * 10^4
 * s and t consist of lowercase English letters.
 *
 *
 *
 * Follow up: What if the inputs contain Unicode characters? How would you
 * adapt your solution to such a case?
 *
 */

struct Solution;
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut history = HashMap::new();
        s.chars()
            .for_each(|c| *(history.entry(c).or_insert(0)) += 1);
        t.chars()
            .for_each(|c| *(history.entry(c).or_insert(0)) -= 1);
        return history.values().all(|&v| v == 0);
    }
}
// @lc code=end
