#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lptr = 1
        for rptr in range(1, len(nums)):
            if nums[rptr] != nums[rptr -1]:
                nums[lptr] = nums[rptr]
                lptr+=1
        return lptr
# @lc code=end