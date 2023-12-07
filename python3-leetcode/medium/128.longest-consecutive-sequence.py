#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in nset:
                length = 0
                while(n+length) in nset:
                    length += 1
                longest = max(longest, length)
        return longest
# @lc code=end

def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0
    nums.sort()
    mlength = 1
    length = 1

    for n in range(1, len(nums)):
        if nums[n-1] == nums[n] - 1:
            length += 1
        elif nums[n-1] != nums[n]:
            length = 1
        mlength = max(mlength, length)

    return mlength

