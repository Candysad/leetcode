#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        dp[i] 表示当前可以表达的种类
        dp[i] = 
            dp[i-1]， i 单独为一个字 （如果可以，即当前位置不能是0）
        +   dp[i-2]， i 和前一个一起组成一个字(如果可以， 即当前2个字组成 处于 [10, 26] 中) 
        
        如果两个条件都不满足，那就是0
        那么后面的结果也会顺位保持是0，也就是最后没有答案 
        '''
        if s[0] == '0':
            return 0
        
        s = [int(c) for c in s]
        n = len(s)
        dp = [0] * (n+1) # 因为2个一组的还要再往前看一点，所以需要一个虚空开头
        dp[0] = 1 # 虚空开头 1 种
        dp[1] = 1 # 第一个数自己 1 种
        
        def char2(n1, n2):
            if n1 == 1:
                return True
            if n1 == 2 and 0 <= n2 <= 6:
                return True
            
            return False
                
        for i in range(2, n+1):
            if s[i-1] != 0:
                dp[i] = dp[i-1]
            
            if char2(s[i-2], s[i-1]):
                dp[i] += dp[i-2]
        # print(dp)
        return dp[-1]
# @lc code=end

