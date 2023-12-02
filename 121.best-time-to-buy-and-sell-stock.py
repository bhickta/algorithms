#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lptr, mprofit, rptr = 0, 0, 1
        while(rptr < len(prices)):
            cprofit = prices[rptr] - prices[lptr]
            if cprofit < 0:
                lptr = rptr
            rptr += 1
            mprofit = max(mprofit, cprofit)
        return mprofit
# @lc code=end
