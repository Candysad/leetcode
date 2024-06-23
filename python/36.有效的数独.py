#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def nineSquare(x, y):
            result = set()
            appear = 0
            for i in range(3):
                for j in range(3):
                    if board[x+i][y+j] != '.':
                        appear += 1
                        result.add(board[x+i][y+j])
            if appear == len(result):
                return True
            return False
        
        def column(j):
            result = set()
            appear = 0
            for i in range(9):
                if board[i][j] != '.':
                    result.add(board[i][j])
                    appear += 1
            if appear == len(result):
                return True
            return False

        def row(i):
            result = set()
            appear = 0
            for j in range(9):
                if board[i][j] != '.':
                    result.add(board[i][j])
                    appear += 1
            if appear == len(result):
                return True
            return False
        
        for i in range(9):
            if not row(i): return False
        for j in range(9):
            if not column(j): return False
        
        for i in range(3):
            for j in range(3):
                x = 3 * i
                y = 3 * j
                if not nineSquare(x, y): return False
        
        return True
        
        
# @lc code=end