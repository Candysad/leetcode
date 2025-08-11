#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        立即推肯定每行每列分别有一个
        
        最符合直觉则用数组
        也可以用位运算
        
        每次斜着和列都不能用的地方排除
        然后在剩余的位置里选一个
        然后更新
        
        用递归往下走，实现回溯
        '''
        def generate_board(record):
            board = [['.']*n for _ in range(n)]
            for i, j in enumerate(record):
                board[i][j] = 'Q'
            return [''.join(line) for line in board]
        
        full = 2 ** n - 1
        result = []
        record = [0] * n
        def dfs(i, cs, lcross, rcross):
            if i == n:
                result.append(generate_board(record))
                return

            now = cs | lcross | rcross
            for j in range(n):
                if ((now >> j) & 1) == 0:
                    record[i] = j
                    
                    tl = (lcross << 1) | (1 << (j+1))
                    tr = (rcross >> 1) | ((1 << (j-1)) if j > 0 else 0)
                    tcs = cs | (1 << j)
                    dfs(i+1, tcs, tl, tr)
                    
                    record[i] = 0
        
        dfs(0, 0, 0, 0)
        return result
# @lc code=end

