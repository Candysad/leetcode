#
# @lc app=leetcode.cn id=2732 lang=python3
#
# [2732] 找到矩阵中的好子集
#
from collections import defaultdict
# @lc code=start
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        '''
        数学题
        最好是恰好有一个全0的行
        
        或者恰有2行 & 为0
        
        否则无解
        '''
        m = len(grid)
        n = len(grid[0])
        
        def encode(row:list):
            result = 0
            for j in range(n):
                result += row[j] << (n-1-j)
            return result

        table = defaultdict(list)
        for i in range(m):
            row = encode(grid[i])
            if row == 0:
                return [i]
            else:
                if not table[row]: table[row].append(i)
        
        for i in table.keys():
            for j in table.keys():
                if i & j == 0:
                    return [table[i][0], table[j][0]]
        return []     
# @lc code=end