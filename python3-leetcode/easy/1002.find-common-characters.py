#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    #  "Counter Intersection" approach
    def commonChars(self, words: list[str]) -> list[str]:
        from collections import Counter
        if not words:
            return []
        common_counter = Counter(words[0])

        for word in words[1:]:
            word_counter = Counter(word)
            common_counter &= word_counter

        result = []
        for char, count in common_counter.items():
            result.extend([char] * count)

        return result

# @lc code=end
Solution().commonChars(['nishant', 'bhickta', 'bnita'])

# The "Minimum Frequency" or "Minimum Count" approach 
def commonChars(self, A: list[str]) -> list[str]:
    if len(A)<2 : return A
    m_count = [math.inf] * 26
    for word in A:
        cur_count = [0] * 26
        for c in word:
            cur_count[ord(c) - ord('a')] += 1
        for c in range(26):
            m_count[c] = min(cur_count[c], m_count[c])
    res = []
    for c in range(26):
        for _ in range(m_count[c]):
            res.append(chr(c+ord('a')))
    return res

def commonChars(self, A: list[str]) -> list[str]:
    if len(A)<2 : return A
    alist = set(A[0])
    res = []
    for one in alist:
        n = min([a_word.count(one) for a_word in A])
        if n:
            res += [one]*n
    return res