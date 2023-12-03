#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if count == 0:
                    continue
                else:
                    break
            else:
                count += 1
        return count
# @lc code=end

    def lengthOfLastWord(self, s: str) -> int:
        word = [word for word in s.split() if word.split()]
        return len(word[-1])
