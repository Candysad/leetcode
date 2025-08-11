#
# @lc app=leetcode.cn id=1329 lang=python3
#
# [1329] 将矩阵按对角线排序
#

# @lc code=start
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        
        # 顶上开始
        for i in range(m):
            t = []
            j, k = 0, i
            while j < n and k < m:
                t.append(mat[j][k])
                j += 1
                k += 1
            t.sort(reverse=True)
            
            j, k = 0, i
            while j < n and k < m:
                mat[j][k] = t.pop()
                j += 1
                k += 1
            
        # 左边一列
        for i in range(1, n):
            t = []
            j, k = i, 0
            while j < n and k < m:
                t.append(mat[j][k])
                j += 1
                k += 1
            t.sort(reverse=True)
            
            j, k = i, 0
            while j < n and k < m:
                mat[j][k] = t.pop()
                j += 1
                k += 1
        return mat
        
# @lc code=end

