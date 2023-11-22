#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        rows = [[] for row in range(numRows)]
        index = 0
        step = 1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        for i in range(len(rows)):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)
# @lc code=end
def convert(self, s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s): return s
    res = ""
    for r in range(numRows):
        increment = 2 * (numRows - 1)
        for i in range(r, len(s), increment):
            res += s[i]
            if(r>0 and r<numRows -1 and i + increment - 2 * r < len(s)):
                res += s[i + increment - 2 * r]
    return res
