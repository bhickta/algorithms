#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = set()
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    if (i, element) in res or (element, j) in res or (i // 3, j // 3, element) in res :
                        return False
                    res.add((i, element))
                    res.add((element, j))
                    res.add((i // 3, j // 3, element))
        return True
# @lc code=end

def isValidSudoku(self, board: List[List[str]]) -> bool:
    res = []
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if x != '.':
                res += [(i, x), (x, j), (i // 3, j // 3, x)]
    return len(res) == len(set(res))

def isValidSudoku(self, board):
    res = []
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != '.':
                res += [(i, element), (element, j), (i // 3, j // 3, element)]
    return len(res) == len(set(res))
    
    res = []
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != '.':
                res.append((i, element))
                res.append((element, j))
                res.append((i // 3, j // 3, element))
    return len(res) == len(set(res))

def isValidSudoku(self, board: List[List[str]]) -> bool:
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                target = board[i][j]
                target_i, target_j = i, j
            else:
                continue

            for k in range(9):
                if target_j == k:
                    continue
                else:
                    if target == board[i][k]:
                        return False

            for l in range(9):
                if target_i == l:
                    continue
                else:
                    if target == board[l][j]:
                        return False

            for n in range(9):
                for m in range(9):
                    if n == target_i and m == target_j:
                        continue

                    if n // 3 == target_i // 3 and m // 3 == target_j // 3:
                        if target == board[n][m]:
                            return False
    return True


def isValidSudoku(self, board: List[List[str]]) -> bool:
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[r // 3, c // 3].add(board[r][c])
    return True
