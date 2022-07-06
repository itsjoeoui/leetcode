/*
 * @lc app=leetcode id=509 lang=typescript
 *
 * [509] Fibonacci Number
 */

// @lc code=start
function fib(n: number): number {
  if (n < 2) return n;

  let fib1 = 0,
    fib2 = 1,
    tmp = 0;

  for (let i = 2; i <= n; i++) {
    tmp = fib1;
    fib1 = fib2;
    fib2 = tmp + fib1;
  }

  return fib2;
}
// @lc code=end
