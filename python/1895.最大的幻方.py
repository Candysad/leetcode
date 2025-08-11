#
# @lc app=leetcode.cn id=1895 lang=python3
#
# [1895] 最大的幻方
#

# @lc code=start
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 or n == 1:
            return 1
        rows = [[grid[0][0]]]
        columns = [[grid[0][j]] for j in range(n)]

        for j in range(1, n):
            rows[0].append(rows[0][-1] + grid[0][j])
            
        for i in range(1, m):
            rows.append([grid[i][0]])
            columns[0].append(columns[0][-1] + grid[i][0])
            for j in range(1, n):
                rows[i].append(rows[i][-1] + grid[i][j])
                columns[j].append(columns[j][-1] + grid[i][j])   
        
        result = 1
        for i in range(m):
            if m-i <= result: break
            for j in range(n):
                if n-j <= result: break

                for k in range(min(1, result), min(m-i, n-j)):
                    # 行
                    trow = rows[i][j+k] - rows[i][j] + grid[i][j]
                    for ti in range(i+1, i+k+1):
                        if trow != rows[ti][j+k] - rows[ti][j] + grid[ti][j]:
                            trow = -1
                            break
                    if trow == -1: continue

                    # 列
                    tcolumn = columns[j][i+k] - columns[j][i] + grid[i][j]
                    if tcolumn != trow: continue
                    for tj in range(j+1, j+k+1):
                        if tcolumn != columns[tj][i+k] - columns[tj][i] + grid[i][tj]:
                            tcolumn = -1
                            break
                    if tcolumn == -1: continue

                    # 主对角线
                    tcross1 = 0
                    ti, tj = i, j
                    while ti <= i+k:
                        tcross1 += grid[ti][tj]
                        ti += 1
                        tj += 1

                    # 副对角线
                    if trow == tcross1:
                        tcross2 = 0
                        ti, tj = i, j+k
                        while ti <= i+k:
                            tcross2 += grid[ti][tj]
                            ti += 1
                            tj -= 1
 
                        if tcross2 == tcross1:
                            result = max(result, k+1)
        return result
# @lc code=end

