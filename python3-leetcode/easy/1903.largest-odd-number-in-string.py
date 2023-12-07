#
# @lc app=leetcode id=1903 lang=python3
#
# [1903] Largest Odd Number in String
#


# @lc code=start
class Solution:
    def largestOddNumber(self, num: str) -> str:
        lss = ""
        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                lss = num[:i+1] if len(num[:i+1]) > len(lss) else lss
        return lss
# @lc code=end