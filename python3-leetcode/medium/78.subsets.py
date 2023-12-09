#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums):
        pset = [[]]
        for num in nums:
            i = 0
            n = len(pset)
            while i < n:
                sset = pset[i].copy()
                sset.append(num)
                pset.append(sset)
                i += 1
        return pset

# @lc code=end

def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res

class Solution:
    def subsets(self, nums):
        pset = []
        self.dfs(nums, [], pset)
        return pset

    def dfs(self, nums, subset, pset):
        pset.append(subset)
        for i in range(len(nums)):
            self.dfs(nums[i + 1 :], subset + [nums[i]], pset)
