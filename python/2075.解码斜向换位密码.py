#
# @lc app=leetcode.cn id=2075 lang=python3
#
# [2075] 解码斜向换位密码
#

# @lc code=start
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        columns = n // rows
        
        result = []
        for j in range(columns):
            for i in range(rows):
                if i*columns + i+j >= n:
                    break
                result.append(encodedText[i*columns + i+j])
        
        result = ''.join(result).rstrip()
        return result
        
# @lc code=end

