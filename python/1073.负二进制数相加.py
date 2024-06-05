#
# @lc app=leetcode.cn id=1073 lang=python3
#
# [1073] 负二进制数相加
#

# @lc code=start
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = len(arr1)
        n = len(arr2)
        num1 = 0
        num2 = 0
        for i in range(max(m, n)):
            if i < m:
                num1 += num1[i] * (-2)**i
            if i < n:
                num2 += num2[i] * (-2)**i
        num = num1 + num2
        result = []
        while num:
            t1 = num % -2
            t2 = num // -2
            result.append(t1)
            if t1 == -1:
                num = t2 + 1
        return result[::-1]
        
        
# @lc code=end

