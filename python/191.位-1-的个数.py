#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        直接数
        '''
        # count = 0
        # for i in range(32):
        #     if n & (1 << i): # & 按位与
        #         count+=1     # 右侧除了第 i 位是1之外其余为0
        # return count
        
        '''
        进退位比
        进退之后之前最后一位变为0
        仍然一致为0，不一致为1
        '''
        # count = 0
        # while n:
        #     if n >> 1 << 1 != n:
        #         count += 1
        #     n = n >> 1
        # return count
        
        '''
        -1然后按位与
        可以减少循环使次数 < n
        '''
        count = 0
        while n:
            count += 1
            n &= (n-1)
        return count
        
# @lc code=end

