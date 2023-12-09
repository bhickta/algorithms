#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, pd, nd = set(), set(), set()
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or r+c in pd or r-c in nd:
                    continue
                col.add(c)
                pd.add(r+c)
                nd.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)

                col.remove(c)
                pd.remove(r+c)
                nd.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res

# @lc code=end

