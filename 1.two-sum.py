#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [i, map[complement]]
            map[nums[i]] = i
        return []
# @lc code=end

