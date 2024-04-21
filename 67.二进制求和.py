#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        二进制加法
        递归(按位异或+进位)
        字符串正着放
        倒着遍历
        '''
        length = max(len(a), len(b)) + 1
        a = "0"*(length-len(a)) + a
        b = "0"*(length-len(b)) + b

        def xorAcarry(x1, x2):
            carry = ["0"]*length
            result = ["0"]*length
            for i in range(length-1, -1, -1):
                if x1[i] == x2[i]:
                    result[i] = "0"
                    if a[i] == "1":
                        carry[i-1] = "1"
                else:
                    result[i] = 1
            return result, carry
        
        result, carry = xorAcarry(a, b)
        while carry != ["0"]*length:
            print(result, carry)
            result, carry = xorAcarry(result, carry)
        return ''.join(result)

       
# @lc code=end
