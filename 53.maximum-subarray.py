#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        cur_sum = 0

        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum
# @lc code=end
def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    max_sum = float('-inf') # fails in case nums[0] is negative hence
    lptr, rptr, cur_sum = 0, 0, 0
    while(rptr < n):
        cur_sum += nums[rptr]
        if cur_sum < 0:
            cur_sum = 0
            lptr += 1
        rptr += 1
        max_sum = max(max_sum, cur_sum)
    return max_sum

def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += nums[k]
            max_sum = max(max_sum, current_sum)

    return max_sum

def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    max_sum = float('-inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum