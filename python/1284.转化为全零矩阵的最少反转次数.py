#
# @lc app=leetcode.cn id=1284 lang=python3
#
# [1284] 转化为全零矩阵的最少反转次数
#

# @lc code=start
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        def encode(mat):
            count = 0
            result = 0
            # 矩阵从低到高从前往后对应编码里的从低到高从后往前
            for i in range(m):
                for j in range(n):
                    result |= mat[i][j] << count
                    count += 1
            return result

        def flip(num, i):
            column = i // n # 当前所在行
            
            num ^= 1 << i# 翻转自己
            # 左
            if (i-1) // n == column:
                num ^= 1 << (i-1)
            # 右
            if (i+1) // n == column:
                num ^= 1 << (i+1)
            # 上
            if column > 0:
                num ^= 1 << (i-n)
            # 下
            if column < m-1:
                num ^= 1 << (i+n)
            return num

        num = encode(mat)
        vis = set()
        vis.add(num)
        queue = [num]
        layer = 0
        while queue:
            t = queue
            queue = []
            for num in t:
                if num == 0:
                    return layer
                
                for i in range(m*n):
                    tnum = flip(num, i)
                    if tnum not in vis:
                        queue.append(tnum)
                        vis.add(tnum)
            layer += 1
        return -1 
# @lc code=end