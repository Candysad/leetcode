#
# @lc app=leetcode.cn id=1914 lang=python3
#
# [1914] 循环轮转矩阵
#

# @lc code=start
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        def alayer(i,k):
            '''
            i 第i层
            (i,i) 每层左上角的坐标
            k 每层要挪的次数
            '''
            # 每层四个角
            lu = (i       , i)
            ld = (m-1 - i , i)
            rd = (ld[0]   , n-1-i)
            ru = (i       , rd[1])
            
            # 总数
            total = 2 * ( (ld[0] - lu[0] + 1) + (ru[1] - lu[1] + 1)) - 4
            k %= total
            if k == 0: # 倍数次挪动等于没挪
                return
                        
            # 遍历一圈把数字都找出来
            layer = []
            j = i
            # 向下
            while (i,j) != ld:
                layer.append(grid[i][j])
                i += 1
            # 向右
            while (i,j) != rd:
                layer.append(grid[i][j])
                j += 1
            # 向上
            while (i,j) != ru:
                layer.append(grid[i][j])
                i -= 1
            #向左
            while (i,j) != lu:
                layer.append(grid[i][j])
                j-=1
            
            # 挪动
            layer[:] = layer[-k:] + layer[:-k]
            
            # 填回去
            i, j = lu
            t = 0
            # 向下
            while (i,j) != ld:
                grid[i][j] = layer[t]
                t += 1
                i += 1
            # 向右
            while (i,j) != rd:
                grid[i][j] = layer[t]
                t += 1
                j += 1
            # 向上
            while (i,j) != ru:
                grid[i][j] = layer[t]
                t += 1
                i -= 1
            #向左
            while (i,j) != lu:
                grid[i][j] = layer[t]
                t += 1
                j -= 1
        for i in range(min(m // 2, n // 2)):
            alayer(i, k)
        return grid
# @lc code=end

