#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        fmax, smax = -1, -1
        for i in range(len(nums)):
            if nums[i] > fmax:
                smax = fmax
                fmax = nums[i]
            elif nums[i] > smax:
                smax = nums[i]
        return (smax - 1)*(fmax - 1)

# @lc code=end