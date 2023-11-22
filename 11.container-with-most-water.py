#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        curmax = 0
        while l < r:
            mheight = min(height[l], height[r])
            curmax = max(curmax, mheight * (r - l))
            if height[l] <= height[r]:
                l +=1
            else:
                r -= 1
        return curmax

# @lc code=end

def maxArea(self, height: List[int]) -> int:
    res = 0
    for l in range(len(height)):
        for r in range(l+1, len(height)):
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
    return res