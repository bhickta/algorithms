#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        reslen = 0
        for i in range(0, len(s)):
            lptr, rptr = i, i
            while lptr >=0 and rptr < len(s) and s[lptr] == s[rptr]:
                if rptr - lptr + 1 > reslen:
                    res = s[lptr:rptr+1]
                    reslen = rptr - lptr + 1
                lptr -= 1
                rptr += 1

            lptr, rptr = i, i + 1
            while lptr >=0 and rptr < len(s) and s[lptr] == s[rptr]:
                if rptr - lptr + 1 > reslen:
                    res = s[lptr:rptr+1]
                    reslen = rptr - lptr + 1
                lptr -= 1
                rptr += 1
        return res
# @lc code=end

Solution().longestPalindrome(s="abbababccab")

