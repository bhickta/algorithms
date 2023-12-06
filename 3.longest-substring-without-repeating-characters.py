#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_string = ''
        ans = 0
        for c in s:
            if c not in max_sub_string:
                max_sub_string += c
                ans = max(ans, len(max_sub_string))
            else:
                max_sub_string = max_sub_string[max_sub_string.index(c) + 1:] + c
        return ans
# @lc code=end
def lengthOfLongestSubstring(self, s: str) -> int:
    sstr = set()
    left = 0
    ans = 0
    for right in range(len(s)):
        while s[right] in sstr:
            sstr.remove(s[left])
            left += 1
        sstr.add(s[right])
        ans = max(ans, right - left + 1)
    return ans
