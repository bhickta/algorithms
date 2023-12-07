#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
# @lc code=end

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    fq = {}
    for num in nums:
        if num not in fq:
            fq[num] = 1
        else:
            fq[num] += 1
    sorted_fq = sorted(fq.items(), key=lambda x: x[1], reverse=True)
    ret = [key for key, value in sorted_fq[:k]]
    return ret