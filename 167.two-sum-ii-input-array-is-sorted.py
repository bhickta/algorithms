#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while(start<=end):
            sum_start_end = numbers[start] + numbers[end]
            if target == sum_start_end :
                return [start + 1, end + 1]
            elif target < sum_start_end:
                end -= 1
            elif target > sum_start_end:
                start +=1
# @lc code=end