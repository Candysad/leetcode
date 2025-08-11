#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        异或是不进位的加
        进位发生在都是1的位
        把进位的部分加进去
        然后再递归处理新出现的都是1的位
        不适用python 因为整型是无限长的负数不会溢出得到补码
        int getSum(int a, int b) {
            return b == 0 ? a : getSum(a ^ b, (unsigned int)(a & b) << 1);
        }
        '''
        
        # python 用循环手动设置补码
        MASK1 = 2048  # 2^32 符号位
        MASK2 = 1024  # 2^31 最大数值
        MASK3 = 1023 # 2^31-1
        
        a %= MASK1
        b %= MASK1
        while b != 0:
            carry = ((a & b) << 1) % MASK1 # 进位情况
            a = (a ^ b) % MASK1 # 异或
            b = carry # 进位
        # 处理负数
        if a & MASK2:  # 去除符号
            return ~(a ^ MASK2 ^ MASK3)
        else:  # 正数
            return a   
# @lc code=end