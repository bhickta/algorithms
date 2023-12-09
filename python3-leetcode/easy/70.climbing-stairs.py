#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            tmp = two
            two = one + two
            one = tmp
        return two
# @lc code=end

def climbStairs_bruteforce(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return climbStairs_bruteforce(n-1) + climbStairs_bruteforce(n-2)

def climbStairs_memoization(n, memo={}):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n in memo:
        return memo[n]
    else:
        memo[n] = climbStairs_memoization(n-1, memo) + climbStairs_memoization(n-2, memo)
        return memo[n]