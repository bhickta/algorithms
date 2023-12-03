#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        if n == 0:
            return 0
        if n < 3:
            return 1
        if n in memo:
            return memo[n]

        memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return memo[n]
# @lc code=end
s = Solution()
s.fib(5)

def fib(self, n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c

def fib(self, n: int) -> int:
    if n == 0:
        return 0
    if n < 3:
        return 1
    memo = {1: 1, 2: 1}
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]