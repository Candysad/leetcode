#
# @lc app=leetcode.cn id=2266 lang=python3
#
# [2266] 统计打字方案数
#
from collections import defaultdict, deque
from itertools import pairwise
# @lc code=start
d3 = [1, 1, 2]
d4 = [1, 1, 2, 4]
mod = 10 ** 9 + 7
for i in range(1, 10**5 - 3):
    d3.append(sum(d3[-3:]) % mod)
    d4.append(sum(d3[-4:]) % mod)
    
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 10 ** 9 + 7
        coins = lambda x: 3 if x != '7' and x != '9' else 4
        
        '''
        记录哪些要计算，最后集中算
        '''
        # table = defaultdict(lambda : defaultdict(int))
        # lasti = 0
        # n = len(pressedKeys)
        # for i in range(1, n):
        #     if pressedKeys[i] != pressedKeys[i-1]:
        #         table[coins(pressedKeys[lasti])][i-lasti] += 1
        #         lasti = i
        # table[coins(pressedKeys[lasti])][n-lasti] += 1

        # result = 1
        # if table[3]:
        #     d3 = max(table[3].keys())
        #     dp = deque([0,0,1])
        #     for i in range(1, d3 + 1):
        #         t = sum(dp)
        #         if i in table[3]:
        #             result *= t ** table[3][i]
        #             result %= mod
        #         dp.popleft()
        #         dp.append(t)
        
        # if table[4]:
        #     d4 = max(table[4].keys())
        #     dp = deque([0,0,0,1])
        #     for i in range(1, d4 + 1):
        #         t = sum(dp)
        #         if i in table[4]:
        #             result *= t ** table[4][i]
        #             result %= mod
        #         dp.popleft()
        #         dp.append(t)
            
        # return result
        
        '''
        提前算好
        '''
        lasti = 0
        result = 1
        n = len(pressedKeys)
        for i in range(1, n):
            if pressedKeys[i] != pressedKeys[i-1]:
                if coins(pressedKeys[lasti]) == 3:
                    result *= d3[i-lasti]
                    result %= mod
                else:
                    result *= d4[i-lasti]
                    result %= mod
                lasti = i
        if coins(pressedKeys[lasti]) == 3:
            result *= d3[n-lasti]
            result %= mod
        else:
            result *= d4[n-lasti]
            result %= mod
        
        return result
        
        
# @lc code=end