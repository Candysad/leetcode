#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 可被三整除的最大和
#
from math import inf
# @lc code=start
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        '''
        DP
        '''
        dp = [0, -inf, -inf]
        for n in nums:
            m = n % 3
            if m == 0:
                dp = [dp[0] + n, dp[1] + n, dp[2] + n]
            elif m == 1:
                dp = [max(dp[0], dp[2] + n), max(dp[1], dp[0] + n), max(dp[2], dp[1] + n)]
            else:
                dp = [max(dp[0], dp[1] + n), max(dp[1], dp[2] + n), max(dp[2], dp[0] + n)]
        return dp[0]
        
        
        
        '''
        数学解法
        '''
        nums.sort()
        
        queue1 = []
        q1 = 0
        queue2 = []
        q2 = 0
        _sum = 0
        for n in nums:
            _sum += n
            m = n % 3
            if m == 1:
                if len(queue1) < 2:
                    queue1.append(n)
                q1 += 1
            elif m == 2:
                if len(queue2) < 2:
                    queue2.append(n)
                q2 += 1
        
        # 可以都三个一组或者一一对应
        if q1 % 3 == q2 % 3:
            return _sum
        
        # 个数对不上，有空余
        def tails(q1, q2, queue1, queue2):
            m1, m2 = q1 % 3, q2 % 3
            if m1 < m2:
                q1, q2 = q2, q1
                m1, m2 = m2, m1
                queue1, queue2 = queue2, queue1
            # 1-0
            if m1 == 1 and m2 == 0:
                q11 = queue1[0]
                if q2: # 有余数为2的，不是没有
                    q21, q22 = queue2[0], queue2[1]
                    return _sum - q21 - q22 if q11 > q21 + q22 else _sum - q11
                else:
                    return _sum - q11
            
            # 2-0
            elif m1 == 2 and m2 == 0:
                q11, q12 = queue1[0], queue1[1]
                if q2:
                    q21 = queue2[0]
                    return _sum - q21 if q11 + q12 > q21 else _sum - q11 - q12
                else:
                    return _sum - q11 - q12
            
            # 2-1
            else:
                q11 = queue1[0]
                if q2 > 1:
                    q21, q22 = queue2[0], queue2[1]
                    return _sum - q21 - q22 if q11 > q21 + q22 else _sum - q11
                else:
                    return _sum - q11
        return tails(q1, q2, queue1, queue2)
# @lc code=end

