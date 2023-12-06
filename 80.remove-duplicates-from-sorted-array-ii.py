#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        lptr, rptr = 0, 0
        while rptr < len(nums):
            count = 1
            while rptr+1 < len(nums) and nums[rptr] == nums[rptr + 1]:
                rptr += 1
                count += 1
            for i in range(min(2, count)):
                nums[lptr] = nums[rptr]
                lptr +=1
            rptr +=1
        return lptr
# @lc code=end

Solution().removeDuplicates(nums=[1, 1, 1, 3, 3, 4, 4, 4, 4, 6, 6, 8, 9])