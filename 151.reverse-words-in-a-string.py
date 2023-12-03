#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        s = s.strip()
        words = [word for word in re.split(r'\s+', s)]
        words.reverse()
        return " ".join(words)
# @lc code=end

def reverseWords(self, s: str) -> str:
    import re
    words = [word for word in re.split(r'\s+', s) if word]
    words.reverse()
    return " ".join(words)

def reverseWords(self, s: str) -> str:
    words = s.split()
    words = [word.strip() for word in words if word.strip()]
    words.reverse()
    return " ".join(words)