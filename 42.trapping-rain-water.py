#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        water = 0
        n = len(height)
        lmax, rmax = [0] * n, [0] * n
        lhmax, rhmax = height[0], height[n - 1]
        for i in range(1, n):
            lhmax = max(lhmax, height[i - 1])
            lmax[i] = lhmax
            rhmax = max(rhmax, height[n - i])
            rmax[n - i - 1] = rhmax

        for i in range(n):
            water += max(0, min(lmax[i], rmax[i]) - height[i])

        return water
# @lc code=end

def trap(self, height: List[int]) -> int:
    water = 0
    lptr, rptr = 0, len(height) - 1
    lmax, rmax = height[lptr], height[rptr]
    while(lptr < rptr):
        if lmax <= rmax:
            lptr +=1
            lmax = max(lmax, height[lptr])
            water += lmax - height[lptr]
        else:
            rptr -=1
            rmax = max(rmax, height[rptr])
            water += rmax - height[rptr]
    return water

def trap(self, height: list[int]) -> int:
    water = 0
    lmax, rmax = [0], [0]
    lhmax, rhmax = height[0], height[len(height) - 1]
    for i in range(1, len(height)):
        lhmax = max(lhmax, height[i - 1])
        lmax.append(lhmax)
    for i in range(len(height) - 2, -1, -1):
        rhmax = max(rhmax, height[i+1])
        rmax.append(rhmax)
    rmax.reverse()
    for i in range(0, len(height) - 1):
        water += max(0, min(lmax[i], rmax[i]) - height[i])
    return water