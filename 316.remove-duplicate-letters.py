#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        counter = Counter(s)
        stack = []
        seen = set()

        for l in s:
            counter[l] -= 1

            if l in seen:
                continue

            while stack and counter[stack[-1]] > 0 and l < stack[-1]:
                seen.remove(stack.pop())

            stack.append(l)
            seen.add(l)

        return ''.join(stack)
# @lc code=end

Solution().removeDuplicateLetters(s='cbacdcbc')