#
# @lc app=leetcode.cn id=2718 lang=python3
#
# [2718] 查询后矩阵的和
#

# @lc code=start
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row = set()
        column = set()
        result = 0
        for t, i, v in queries[::-1]:
            if t == 0 and i not in row:
                result += v * (n - len(column))
                row.add(i)
            elif t == 1 and i not in column:
                result += v * (n - len(row))
                column.add(i)
            
            if len(row) == n or len(column) == n:
                break
        return result
# @lc code=end

