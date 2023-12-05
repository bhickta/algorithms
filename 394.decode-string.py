#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        numstk, strstk = [], []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num = ''
                j = i
                while j < len(s) and s[j].isnumeric():
                    num += s[j]
                    j += 1
                numstk.append(int(num))
                i = j
            elif s[i] != ']':
                strstk.append(s[i])
                i += 1
            else:
                st = ''
                while strstk[-1] != '[':
                    st = strstk.pop() + st
                strstk.pop()
                rep = numstk.pop()
                st = st * rep
                strstk.append(st)
                i += 1

        return ''.join(strstk)

# @lc code=end

Solution().decodeString(s="100[20[let]20[code]]")

