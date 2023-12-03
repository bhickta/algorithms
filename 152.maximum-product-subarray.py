#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cmax, cmin = 1, 1
        for n in nums:
            if n == 0:
                cmax, cmin = 1, 1
                continue
            tmax = cmax*n
            cmax = max(n, tmax, cmin*n)
            cmin = min(n, tmax, cmin)
            res = max(res, cmax)
        return res
# @lc code=end

