#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            maps, mapt = {}, {}
            for i in range(len(s)):
                if s[i] in maps:
                    maps[s[i]] += 1
                else:
                    maps[s[i]] = 1
                if t[i] in mapt:
                    mapt[t[i]] += 1
                else:
                    mapt[t[i]] = 1
            for c in maps:
                if maps[c] != mapt.get(c, 0):
                    return False
            return True
# @lc code=end

def isAnagram(self, s: str, t: str) -> bool:
    from collections import Counter
    return Counter(s) == Counter(t)

def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    cs, ct = {}, {}

    for i in range(len(s)):
        cs[s[i]] = 1 + cs.get(s[i], 0)
        ct[t[i]] = 1 + ct.get(t[i], 0)
    for c in cs:
        if cs[c] != ct.get(c, 0):
            return False
    return True
