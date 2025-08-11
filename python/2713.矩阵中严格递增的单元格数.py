#
# @lc app=leetcode.cn id=2713 lang=python3
#
# [2713] 矩阵中严格递增的单元格数
#
from math import inf
# @lc code=start
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        queue = []
        for i in range(m):
            for j in range(n):
                queue.append((mat[i][j], i, j))
        # 取所有格子，排序
        queue.sort(key=lambda x: x[0])
        
        # 记录行列上一步
        # (上一个数, 横着走最大, 竖着走最大)
        columns = [(inf, 0, 0) for _ in range(m)]
        rows    = [(inf, 0, 0) for _ in range(n)]
        
        result = 0
        # 从大到小遍历，只从比自己大的地方来
        for num, i, j in queue[::-1]:
            dc, dr = 1, 1
            # 行
            cnum, c, r = columns[i]
            if cnum != num: # 数字不重复
                dc = max(c, r) + 1
            else: # 数字重复，则只能取同一行的
                dc = c
            
            # 列
            rnum, c, r = rows[j]
            if rnum != num:
                dr = max(c, r) + 1
            else:
                dr = r
            
            # 更新
            # 若是同一行数字相同，则可能没有取到上一回竖着走的最大值
            # 所以行列更新都要和当前的横竖走法比较
            columns[i] = (num, max(columns[i][1], dc), max(columns[i][2], dr))
            rows[j] = (num, max(rows[j][1], dc), max(rows[j][2], dr))
            result = max(dc, dr, result)

        return result
# @lc code=end