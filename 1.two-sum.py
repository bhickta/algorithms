#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:

# @lc code=end

def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i +=1
    return []
def twoSum(self, nums: List[int], target: int) -> List[int]:
    map = {}
    for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in map:
            return [i, map[complement]]
        map[nums[i]] = i
    return []