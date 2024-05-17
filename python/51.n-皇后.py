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
        result = []
        
        def generate_board(record):
            '''
            将会用一个长为n的数组存第i行第j列放了
            '''
            board = [['.']*n for _ in range(n)]
            for i, j in enumerate(record):
                board[i][j] = 'Q'
            return [''.join(line) for line in board]
            
        
        # cloumns  标记当前哪些列不能用
        # left     标记当前哪些位置斜左下不能用
        # right    斜右下角
        full = 2**(n+1) - 1 # 满值
        def dfs(columns, left, right, layer, record):
            if layer == n: # 抵达最后一层，每一层都放了
                result.append(generate_board(record))
                return 
            
            now = columns | left | right # 把不能放的位置都合起来
            if now == full: # 没抵达最后一层，但是当前层满了放不了
                return


            left <<= 1  # 只用看n位，超出去了就不用管了
            right >>= 1 # 斜着的每行要再斜着走一步
            # 递归进下一层
            for i in range(n): # 只用看n位
                if ((now >> i) & 1) == 0: # 这里末尾是0才判断为 True 能放
                    record[layer] = n-i-1 # 棋盘从左向右标记，位值从右向左遍历，其实可以直接用i，但是反直觉
                    tc = columns | (1 << i)
                    tleft = left | (1 << (i+1))
                    tright = right | (1 << (i-1)) if i > 0 else right
                    dfs(tc, tleft, tright, layer+1, record)
                    # 下一个可行的位置会再回到 record[layer],修改这个值实现回溯和分支搜索
        dfs(0, 0, 0, 0, [0]*n)
        return result
# @lc code=end

