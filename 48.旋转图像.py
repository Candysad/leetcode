#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        final = n // 2
        i, l = 0, n-1
        #(i, i) 左上角坐标
        # l 单边长度
        while i != final:
            for k in range(i, i+l):
                # Python 同时赋值实现四个角移动
                # 上          # 右            # 下                      # 左
                matrix[i][k], matrix[k][i+l], matrix[n-1-i][2*i+l - k], matrix[n-1 - k][i] = matrix[n-1 - k][i], matrix[i][k], matrix[k][i+l], matrix[n-1-i][2*i+l - k]
                
            l -= 2
            i += 1
# @lc code=end

