#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        对要求顺序的数分组按位置取余数
        '''
        # if numRows == 1:
        #     return s
        
        # span = numRows + numRows - 2
        
        # result = [
        #     ['' for i in range((len(s) // span + 1) * (1 + numRows - 2) )]
        #     for j in range(numRows)
        # ] # 目标矩阵，空间复杂度 O(m*n)
        #   # 最后用 join 合起来 
        
        # for i in range(len(s)):
        #     n = i // span # 当前第 n 组（前面有几组）
        #     m = i % span # 当前组第 m 个
            
        #     # 所在行
        #     row = m if m <= numRows-1 else 2 * numRows - m - 2
        #     # 所在列
        #     column = n * (1 + numRows - 2)
        #     t = m - numRows + 1 if m >= numRows else 0
        #     column += t
            
        #     result[row][column] = s[i]

        # return ''.join([''.join(r) for r in result])
        
        '''
        最后要按行读取，则对要求的行分组
        '''
        if numRows == 1 or len(s) <= numRows:
            return s
        
        result = ['' for i in range(numRows)] # 每行维护一个字符串
                                              # 每次将对应行的新字符添加在后面即可
        now_row = 0             # 当前哪一行
        flag = 1                # 往上往下
        
        for c in s:
            result[now_row] += c
            if now_row == numRows - 1 and flag == 1:
                flag = -1
            elif now_row == 0 and flag == -1:
                flag = 1
            
            now_row += 1 * flag
        return ''.join(result)

# @lc code=end