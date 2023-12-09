#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack: stack.pop()
                elif cur and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c
        return "/" + "/".join(stack)
# @lc code=end