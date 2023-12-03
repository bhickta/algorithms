#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum, lsum = sum(nums), 0
        for i in range(len(nums)):
            rsum -= nums[i]
            if rsum == lsum:
                return i
            else:
                lsum += nums[i]
        return -1
# @lc code=end

