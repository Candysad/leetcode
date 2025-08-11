#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start



class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        
        def alive(num:int):
            '''
            本身存活为正
            本身死了为负数
            
            对于本身存活的
                1 空出来留给本来的1，即1就是本身存活的原始情况
                周围的 1 的数量再 +2 避开 0 和 1
                即如果一个数 num >= 2 则是本身存活且周围1数量为 num-2
            
            如果num是0，就那是本身就是死的0，或者是周围1有0个且本身是死的
            如果num是负数，则绝对值是周围1的数量，本身是死的
            '''
            if num <= 0:
                return 0 
            return 1
        
        def nextCell(i, j):
            nonlocal board, m, n
            # 上
            up = 0 if i == 0 else alive(board[i-1][j])
            # 左上
            upleft = 0 if i == 0 or j == 0 else alive(board[i-1][j-1])
            # 右上
            upright = 0 if i == 0 or j == n - 1 else alive(board[i-1][j+1])
            # 左
            left = 0 if j == 0 else alive(board[i][j-1])
            # 右
            right = 0 if j == n-1 else alive(board[i][j+1])
            # 下
            down = 0 if i == m-1 else alive(board[i+1][j])
            # 左下
            downleft = 0 if i == m-1 or j == 0 else alive(board[i+1][j-1])
            # 右下
            downright = 0 if i == m-1 or j == n-1 else alive(board[i+1][j+1])

            total = up + upleft + upright \
                    + left + right\
                    + down + downleft + downright
            
            board[i][j] = total+2 if board[i][j] else -total
            
        def change(i, j):
            '''
            活细胞周围1少于1多余3会死 # 编码的时候正数右移了2
            死细胞周围1刚好3个变活
            '''
            nonlocal board
            if board[i][j] == -3 or 3 < board[i][j] < 6:
                board[i][j] = 1
            else:
                board[i][j] = 0
            
            

        for i in range(m):
            for j in range(n):
                nextCell(i, j)
        
        for i in range(m):
            for j in range(n):
                change(i, j)
                 

# @lc code=end

