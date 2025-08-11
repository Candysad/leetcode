#
# @lc app=leetcode.cn id=1702 lang=python3
#
# [1702] 修改后的最大二进制字符串
#

# @lc code=start
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        '''
        从第一个0开始，前面的1不动
        找后面的0的个数（包括第一个0）
        把0尽可能放在前面一起，然后全部变成1，只有最后一个0不能变
        '''
        n = len(binary)
        i = 0
        result = ''
        #  找第一个0
        while i < n and binary[i] != '0':
            i += 1
        start = i
        if start == n: # 数到头了都没有
            return binary
        
        # 数一共有多少个0
        zeros = 1
        ones = 0
        i += 1
        while i < n:
            if binary[i] == '0':
                zeros += 1
            else:
                ones += 1
            i += 1
                
        if zeros == 1:# 就一个0，变不了
            return binary

        # 不止一个 0
        # 最开始的 1 不动
        # 从第一个 0 开始放 zeros-1 个 1，和一个 0
        # 最后是原本后面的 1
        return binary[:start] + '1'*(zeros - 1) + '0' + '1'*ones
            
        
# @lc code=end

