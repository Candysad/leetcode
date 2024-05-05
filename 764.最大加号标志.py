#
# @lc app=leetcode.cn id=764 lang=python3
#
# [764] 最大加号标志
#

# @lc code=start
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines = set([ (p[0], p[1]) for p in mines ])
        
        '''
        四个方向的连续1
        0 从上往下
        1 从下往上
        2 从左往右
        3 从右往左
        '''
        directs = [ [ [0] * n  for _ in range(n)]  for __ in range(4) ]
        
        # 从上往下，从左往右，正着遍历
        for i in range(n):
            for j in range(n):
                # 从上往下
                if i == 0:
                    # 最上面
                    if (i, j) not in mines:
                        directs[0][0][j] = 1
                else:
                    directs[0][i][j] = directs[0][i-1][j] + 1 if (i,j) not in mines else 0
                
                # 从左往右
                if j == 0:
                    # 最左边
                    if (i, j) not in mines:
                        directs[2][i][0] = 1
                else:
                    directs[2][i][j] = directs[2][i][j-1] + 1 if (i,j) not in mines else 0
                
        # 从下往上，从右往左，这俩的之前状态下标更大
        # 可以在上面单独算下标然后处理
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                # 从下往上
                if i == n-1:
                    # 最下面
                    if (i, j) not in mines:
                        directs[1][i][j] = 1
                else:
                    directs[1][i][j] = directs[1][i+1][j] + 1 if (i,j) not in mines else 0
                
                # 从右往左
                if j == n-1:
                    # 最右边
                    if (i, j) not in mines:
                        directs[3][i][j] = 1
                else:
                    directs[3][i][j] = directs[3][i][j+1] + 1 if (i,j) not in mines else 0
        
        result = 0
        for i in range(n):
            for j in range(n):
                result = max(result, min(directs[0][i][j], directs[1][i][j], directs[2][i][j], directs[3][i][j]))
        return result
                

        
        '''
        居然能过.....
        '''
        # grid = [[1] * n for _ in range(n)]
        # for p in mines:
        #     grid[p[0]][p[1]] = 0
        
        # def cross(i, j, t):
        #     k = 1
        #     while t:
        #         if grid[i+k][j] and grid[i-k][j] and grid[i][j+k] and grid[i][j-k]:
        #             k += 1
        #             t -= 1
        #         else:
        #             break
        #     return k
        
        # result = 0
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j]:
        #             t = min(i, n-i-1, j, n-j-1)
        #             c = cross(i, j, t)
        #             result = max(result, c)
        #         else:
        #             continue
        # return result
# @lc code=end

