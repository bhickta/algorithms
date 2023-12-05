#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        ptr = len(num) - 1
        carry = 0
        ans = []
        while(ptr >= 0 or k >0 or carry > 0):
            numv = num[ptr] if ptr >=0 else 0
            sum = numv + k%10 + carry
            carry = sum // 10
            ans.append(sum%10)
            ptr -=1
            k = k//10
        ans.reverse()
        return ans
# @lc code=end

Solution().addToArrayForm([2,1,5], 806)