/*
 * @lc app=leetcode id=409 lang=typescript
 *
 * [409] Longest Palindrome
 */

// @lc code=start
function longestPalindrome(s: string): number {
  let track: Set<string> = new Set<string>();
  let count: number = 0;

  for (let entry of s) {
    if (track.has(entry)) {
      track.delete(entry);
      count += 2;
    } else {
      track.add(entry);
    }
  }
  return track.size == 0 ? count : count + 1;
}
// @lc code=end
