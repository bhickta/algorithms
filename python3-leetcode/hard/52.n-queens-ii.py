#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        col, pd, nd = set(), set(), set()
        res = 0
        def backtrack(r):
            if r == n:
                nonlocal res
                res +=1
                return
            for c in range(n):
                if c in col or r+c in pd or r-c in nd:
                    continue
                col.add(c)
                pd.add(r+c)
                nd.add(r-c)
                backtrack(r+1)
                col.remove(c)
                pd.remove(r+c)
                nd.remove(r-c)
        backtrack(0)
        return res
        
# @lc code=end

