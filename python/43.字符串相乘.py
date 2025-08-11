#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# @lc code=start
class Solution:
    '''
    个位数相乘的结果可以接受，不会太长，最多就两位
    用数组直接装对应位的计算结果，免去在后面+0
    最后按位处理进位
    答案数组对于答案来说是正方向的，对于构建来说是反方向的
    
    用数组从低位到高位存, 每个数字加在当前计算的最低位
    m位 n位数字相乘最多 m+n 位
    最后从低位到高位取余得到当前位并向前进位
    '''
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n + 1)
        for i in range(m-1, -1, -1):
            n1 = int(num1[i])
            for j in range(n-1, -1, -1):
                n2 = int(num2[j])
                # 当前最低位是当前位之和，但i和j是倒着数的
                result[m+n-i-j-2] += n1 * n2
        
        for i in range(m + n):
            carry = result[i]// 10
            result[i+1] += carry
            result[i] %= 10

        # 不知道停在哪一位，需要先找一遍
        i = 0
        for j in range(m+n+1):
            if result[j] != 0:
                i = j
            result[j] = str(result[j])
        return ''.join(result[i::-1])
# @lc code=end

    '''
    纯字符串
    意思是中间过程中也可能有大数
    需要把所有位都单独拿出来
    '''
    # def  addStrings(self, num1: str, num2: str) -> str:
    #     '''
    #     两数相加
    #     '''
    #     result = []
    #     i = len(num1)-1
    #     j = len(num2)-1
    #     carry = 0
    #     while i >= 0 or j >= 0 or carry:
    #         n1 = int(num1[i]) if i >= 0 else 0
    #         n2 = int(num2[j]) if j >= 0 else 0
    #         t = n1 + n2 + carry
    #         result.append(str(t % 10))
    #         carry = t // 10
    #         i -= 1
    #         j -= 1 
    #     return ''.join(result[::-1])

    # def multiply(self, num1: str, num2: str) -> str:
    #     if num1 == "0" or num2 == "0":
    #         return "0"
        
    #     result = "0"
    #     for i, n1 in enumerate(num1[::-1]):
    #         n1 = int(n1)
    #         if n1 == 0:
    #             continue
    #         zeroes1 = "0" * i
    #         for j, n2 in enumerate(num2[::-1]):
    #             n2 = int(n2)
    #             if n2 == 0:
    #                 continue
    #             zeroes2 = "0" * j
    #             result = self.addStrings(result, (str(n1 * n2) + zeroes1 + zeroes2))
    #     return result