#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        maxint = 2**31 - 1
        minint = 2**31
        if x > 0:
            while x:
                r = x % 10
                q = x // 10

                ans = 10 * ans + r
                x = q
            return ans if ans < maxint else 0
        else:
            x = abs(x)
            while x:
                r = x % 10
                q = x // 10

                ans = 10 * ans + r
                x = q
            return -ans if ans > minint else 0
# @lc code=end
