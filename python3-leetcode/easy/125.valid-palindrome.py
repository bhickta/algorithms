#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lptr, rptr = 0, len(s) - 1
        while lptr < rptr:
            while lptr < rptr and not self.isalphanum(s[lptr]):
                lptr += 1
            while lptr< rptr and not self.isalphanum(s[rptr]):
                rptr -= 1
            if s[lptr] != s[rptr]:
                return False
            lptr += 1
            rptr -= 1
        return True

    def isalphanum(self, c: str) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("0") <= ord(c) <= ord("9")
            or ord("a") <= ord(c) <= ord("z")
        )

# @lc code=end
def isPalindrome(self, s: str) -> bool:
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
