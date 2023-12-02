#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False

# @lc code=end
def containsDuplicate(self, nums: List[int]) -> bool:
    map = {}
    for num in nums:
        if num in map:
            return True
        else:
            map[num] = False
    return False

def containsDuplicate(self, nums: List[int]) -> bool:
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True
    return False
