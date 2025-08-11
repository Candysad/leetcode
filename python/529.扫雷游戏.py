#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        
        
        def check(i, j):
            t = 0
            for x, y in [
                        (i-1, j-1), (i-1, j), (i-1, j+1),
                        (i,   j-1), (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1)
                    ]:
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'M':
                    t += 1
            board[i][j] = str(t) if t else 'B'
            
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n:
                if board[i][j] == "E":
                    check(i, j)
                    if board[i][j] == "B":
                        for x, y in [
                            (i-1, j-1), (i-1, j),  (i-1, j+1),
                            (i,   j-1), (i,   j+1),
                            (i+1, j-1), (i+1, j),  (i+1, j+1)
                        ]:
                            dfs(x, y)
        
        for line in board:
            print(line)
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
        else:
            dfs(i, j)
            
        for line in board:
            print(line)
        return board
# @lc code=end

